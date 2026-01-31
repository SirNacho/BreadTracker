from schemas.camel_model import CamelModel
from typing import Optional, List            

class GroceryOption(CamelModel):
    title: str
    price: str
    store: str
    thumbnail: Optional[str] = None 

class GroceryListItem(CamelModel):
    user_grocery_item: str
    shopping_results: List[GroceryOption]
    
class GroceryCategory(CamelModel):
    category: str
    items: List[GroceryOption]

class GroceryResponse(CamelModel):
    product_name: str
    categories: List[GroceryCategory]