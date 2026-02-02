from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from db import get_session
from models import GroceryList
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
    groceries = { item: search_serp(item) for item in grocery_list.contents.splitlines() }

    grocery_names = { key: [item.title for item in val] for key, val in groceries.items() }
    
    categorized_groceries = await categorize_groceries(grocery_names)
    
    grocery_options = grocery_list_service.create_grocery_options(groceries, categorized_groceries)
    
    grocery_list = await grocery_list_service.save_grocery_options(session, list_id, grocery_options)
    
    return grocery_list
