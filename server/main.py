from typing import List
from dotenv import load_dotenv
from fastapi import FastAPI

from serp_helpers import search_serp
from models.requests import SerpSearchRequest
from models.responses import GroceryListItem

load_dotenv()

app = FastAPI()

@app.get('/')
def root():
    return { 'message': 'Hello World!' }

@app.post('/search')
def search_grocery_list(request: SerpSearchRequest):
    groceries = {}
    for grocery_item in request.grocery_list.splitlines():
        groceries[grocery_item] = search_serp(grocery_item)
    return groceries
        
                
