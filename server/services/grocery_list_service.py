from typing import Dict, List
from collections import defaultdict
from sqlmodel.ext.asyncio.session import AsyncSession

from schemas.responses import GroceryOption
from models import GroceryList

async def get_grocery_list(session: AsyncSession, grocery_list_id: int) -> GroceryList:
    item = await session.get(GroceryList, grocery_list_id)
    if not item:
        raise Exception(f'Grocery List of id {grocery_list_id} does not exist')
    return item

async def create_grocery_list(session: AsyncSession, grocery_list: GroceryList) -> GroceryList:
    session.add(grocery_list)
    await session.commit()
    await session.refresh(grocery_list)
    return grocery_list

async def update_grocery_list(session: AsyncSession, grocery_list_id: int, contents: str) -> GroceryList:
    item = await get_grocery_list(session, grocery_list_id)
    item.contents = contents
    session.add(item)
    await session.commit()
    return item

def _find_grocery_option_by_title(groceries: Dict[str, List[GroceryOption]], item: str, title: str) -> GroceryOption | None:
    for grocery in groceries[item]:
        if title == grocery.title: return grocery
    return None

def create_grocery_options(groceries: Dict[str, List[GroceryOption]], categorized_groceries: Dict[str, Dict[str, List[str]]]) -> Dict[str, Dict[str, List[GroceryOption]]]:
    # 1. Find the "Common Ground": Which stores have at least ONE result for EVERY search term?
    stores_per_item = {}
    for item, options in groceries.items():
        stores_per_item[item] = {opt.store for opt in options}
    
    # The intersection of all sets gives us stores that carry everything on the list
    if not stores_per_item:
        return {}
        
    complete_stores = set.intersection(*stores_per_item.values())
    
    # 2. Build the options list, but ONLY include items from these complete stores
    grocery_options: Dict[str, Dict[str, List[GroceryOption]]] = defaultdict(lambda: defaultdict(list))
    
    for item, categories in categorized_groceries.items():
        for category, grocery_titles in categories.items():
            for title in grocery_titles:
                grocery_option = _find_grocery_option_by_title(groceries, item, title)
                
                # Check if this option belongs to a store that has the full list
                if grocery_option and grocery_option.store in complete_stores:
                    grocery_options[item][category].append(grocery_option)
    
    # 3. Final Cleanup: Remove categories that became empty after filtering
    final_output = {}
    for item, cats in grocery_options.items():
        # Only keep categories that still have valid options from complete stores
        filtered_cats = {c: opts for c, opts in cats.items() if opts}
        if filtered_cats:
            final_output[item] = filtered_cats
            
    return final_output

async def save_grocery_options(session: AsyncSession, grocery_list_id: int, grocery_options) -> GroceryList:
    grocery_list = await get_grocery_list(session, grocery_list_id)
    
    # Standardizing the dictionary conversion for JSONB
    serialized_data = {}
    for item_name, categories in grocery_options.items():
        serialized_data[item_name] = {}
        for cat_name, options in categories.items():
            serialized_data[item_name][cat_name] = [
                opt.model_dump() if hasattr(opt, "model_dump") else opt 
                for opt in options
            ]
    
    grocery_list.grocery_options = serialized_data
    session.add(grocery_list)
    await session.commit()
    await session.refresh(grocery_list)
    return grocery_list

def find_selected_groceries(grocery_list: GroceryList, skus: Dict[str, str]) -> Dict[str, List[GroceryOption]]:
    selected_grocery_list = {}
    for item, category in skus.items():
        selected_grocery_list[item] = grocery_list.grocery_options[item][category]
    return selected_grocery_list

def sort_grocery_options_by_store(grocery_options: Dict[str, List[GroceryOption]]):
    grocery_options_by_store: Dict[str, Dict[str, List[GroceryOption]]] = defaultdict(lambda: defaultdict(list))
    
    for category, options in grocery_options.items():
        for item in options:
            store_name = item['store'] 
            grocery_options_by_store[category][store_name].append(item)
            
    return grocery_options_by_store

def convert_price_to_float(price: str):
    clean_price = price.replace('$', '').replace(',', '').strip()
    
    return float(clean_price) if clean_price else 0.0
