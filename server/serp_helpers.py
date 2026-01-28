import os
from serpapi import GoogleSearch

from models.serp_response import SerpResponse


def search_serp(grocery_item):
    params = {
        "engine": "google_shopping_light",
        "q": grocery_item,
        "api_key": os.getenv('SERP_API_KEY'),
        'location': '60617'
    }

    search = GoogleSearch(params)
    results: SerpResponse = search.get_dict()
    shopping_results = results["shopping_results"]
    
    serp_response = []

    for result in shopping_results:
        serp_response.append({
            'title': result['title'],   
            'price': result['price'],
            'store': result['source'],
            'thumbnail': result['thumbnail'],
        })
    return serp_response