import os
import httpx
from typing import List
from schemas.responses import GroceryOption

async def search_serp(grocery_item: str) -> List[GroceryOption]:
    url = "https://serpapi.com/search"
    params = {
        "engine": "google_shopping_light",
        "q": grocery_item,
        "api_key": os.getenv('SERP_API_KEY'),
        "location": "60617",
        "gl": "us",
        "hl": "en"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        results = response.json()
    
    raw_shopping_results = results.get("shopping_results", [])
    
    shopping_results = [
        GroceryOption.model_validate({
            'title': result['title'],   
            'price': result['price'],
            'store': result['source'],
            'thumbnail': result.get('thumbnail'),
        }) for result in raw_shopping_results
    ]
    
    return shopping_results