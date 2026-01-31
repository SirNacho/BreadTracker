from schemas.camel_model import CamelModel

class SaveGroceryListRequest(CamelModel):
    contents: str
    
class CreateGroceryListRequest(CamelModel):
    contents: str

class SearchGroceryListRequest(CamelModel):
    grocery_list: str