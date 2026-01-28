from models.camel_model import CamelModel
from typing import Optional, List            

class GroceryOption(CamelModel):
    title: str
    price: str
    store: str
    thumbnail: Optional[str] = None 

class GroceryListItem(CamelModel):
    user_grocery_item: str
    shopping_results: List[GroceryOption]
    