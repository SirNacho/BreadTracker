from fastapi import FastAPI
from dotenv import load_dotenv
from contextlib import asynccontextmanager

from services.serp_helpers import search_serp
from services.chat import categorize_groceries
from schemas import SearchGroceryListRequest
from db import create_db_and_tables
import models

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield
    pass    

app = FastAPI(lifespan=lifespan)

@app.get('/ping')
def ping():
    return { 'message': 'pong' }

@app.post('/search')
async def search_grocery_list(request: SearchGroceryListRequest):
    groceries = { item: search_serp(item) for item in request.grocery_list.splitlines() }

    grocery_names = { key: [item.title for item in val] for key, val in groceries.items() }
    
    categorized_groceries = await categorize_groceries(grocery_names)
    return categorized_groceries
        
                
