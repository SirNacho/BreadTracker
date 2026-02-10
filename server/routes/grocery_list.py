import asyncio
from typing import Dict
from collections import defaultdict
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from db import get_session
from models import GroceryList
from schemas.responses.grocery_list import GroceryOption
from services import grocery_list_service
from services.serp_helpers import search_serp
from services.chat import categorize_groceries
from schemas.requests import SaveGroceryListRequest, CreateGroceryListRequest

router = APIRouter()

@router.get('/{list_id}', response_model=GroceryList)
async def fetch_grocery_list(list_id: int, session: AsyncSession = Depends(get_session)):
    grocery_list = await grocery_list_service.get_grocery_list(session, list_id)
    return grocery_list

@router.post('/create', response_model=GroceryList)
async def make_grocery_list(request: CreateGroceryListRequest, session: AsyncSession = Depends(get_session)):
    grocery_list = GroceryList(contents=request.contents, is_active=True)
    
    grocery_list = await grocery_list_service.create_grocery_list(session, grocery_list)
    return grocery_list

@router.post('/save/{list_id}', response_model=GroceryList)
async def save_grocery_list(list_id: int, request: SaveGroceryListRequest, session: AsyncSession = Depends(get_session)):
    grocery_list = await grocery_list_service.update_grocery_list(session, list_id, request.contents)
    return grocery_list

@router.post('/search/{list_id}', response_model=GroceryList)
async def search(list_id: int, session: AsyncSession = Depends(get_session)):
    grocery_list = await grocery_list_service.get_grocery_list(session, list_id)
    search_terms = grocery_list.contents.splitlines()

    tasks = [search_serp(term) for term in search_terms]
    results = await asyncio.gather(*tasks)
    
    groceries = dict(zip(search_terms, results))

    grocery_names = { key: [item.title for item in val] for key, val in groceries.items() }
    
    categorized_groceries = await categorize_groceries(grocery_names)
    
    grocery_options = grocery_list_service.create_grocery_options(groceries, categorized_groceries)
    
    grocery_list = await grocery_list_service.save_grocery_options(session, list_id, grocery_options)
    
    return grocery_list

@router.post('/select-skus/{list_id}')
async def select_sku(list_id: int, request: Dict[str, str], session: AsyncSession = Depends(get_session)):
    grocery_list = await grocery_list_service.get_grocery_list(session, list_id)
    selected_options = grocery_list_service.find_selected_groceries(grocery_list, request)
    grouped_options = grocery_list_service.sort_grocery_options_by_store(selected_options)
    
    store_items = defaultdict(list)
    store_costs = defaultdict(float)
    
    for _, stores in grouped_options.items():
        for store_name, groceries in stores.items():
            cheapest_item = min(
                groceries, 
                key=lambda g: grocery_list_service.convert_price_to_float(g['price'])
            )
            
            price = grocery_list_service.convert_price_to_float(cheapest_item['price'])
            store_items[store_name].append(cheapest_item)
            store_costs[store_name] += price
            
    if not store_costs: return []

    best_store = min(store_costs, key=store_costs.get)
    
    print({
        'store_items': store_items,
        'store_costs': store_costs,
        'best_store': best_store
    })
    
    return store_items[best_store]
    
    
    
