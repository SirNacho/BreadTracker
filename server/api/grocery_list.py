from fastapi import Depends
from sqlmodel import Session

from main import app
from db import get_session
from schemas import SaveGroceryListRequest, CreateGroceryListRequest
from services.grocery_list_service import get_grocery_list, create_grocery_list, update_grocery_list

@app.get('/grocery-list/{list_id}')
async def fetch_grocery_list(list_id: int, session: Session = Depends(get_session)):
    grocery_list = get_grocery_list(session, list_id)
    return grocery_list

@app.post('/grocery-list/create')
async def make_grocery_list(request: CreateGroceryListRequest, session: Session = Depends(get_session)):
    grocery_list = {
        'contents': request.contents,
        'is_active': True
    }
    grocery_list = create_grocery_list(session, grocery_list)
    return grocery_list
    
    

@app.post('/grocery-list/save/{list_id}')
async def save_grocery_list(list_id: int, request: SaveGroceryListRequest, session: Session = Depends(get_session)):
    grocery_list = update_grocery_list(session, list_id, request.contents)
    return grocery_list