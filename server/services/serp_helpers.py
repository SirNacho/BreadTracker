import os
from serpapi import GoogleSearch
from typing import List  

from schemas import GroceryOption

def search_serp(grocery_item: str) -> List[GroceryOption]:
    params = {
        "engine": "google_shopping_light",
        "q": grocery_item,
        "api_key": os.getenv('SERP_API_KEY'),
        "location": "60617",
        "gl": "us",
        "hl": "en"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    
    raw_shopping_results = results.get("shopping_results", [])
    
    shopping_results = [GroceryOption.model_validate({
        'title': result['title'],   
        'price': result['price'],
        'store': result['source'],
        'thumbnail': result.get('thumbnail'),
    }) for result in raw_shopping_results]
    
    return shopping_results