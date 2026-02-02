import asyncio
from typing import Dict, List
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
    grocery_options: Dict[str, Dict[str, List[GroceryOption]]] = {}
    
    for item, categories in categorized_groceries.items():
        grocery_options[item] = {}
        for category, grocery_titles in categories.items():
            grocery_options[item][category] = []
            for grocery in grocery_titles:
                grocery_option = _find_grocery_option_by_title(groceries, item, grocery)
                if grocery_option is not None:
                    print(grocery) 
                    grocery_options[item][category].append(grocery_option)
    
    return grocery_options

async def save_grocery_options(session: AsyncSession, grocery_list_id: int, grocery_options: Dict[str, Dict[str, List[GroceryOption]]]) -> GroceryList:
    grocery_list = await get_grocery_list(session, grocery_list_id)
    grocery_list.grocery_options = grocery_options
    
    session.add(grocery_list)
    await session.commit()
    print('updated grocery options for grocery list', grocery_list_id)
    
    return grocery_list
