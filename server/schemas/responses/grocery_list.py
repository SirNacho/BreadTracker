from schemas import CamelModel
from typing import Optional            

class GroceryOption(CamelModel):
    title: str
    price: str
    store: str
    thumbnail: Optional[str] = None 