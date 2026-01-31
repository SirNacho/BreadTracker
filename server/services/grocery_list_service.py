from sqlmodel import Session
from models import GroceryList

def get_grocery_list(session: Session, grocery_list_id: int) -> GroceryList:
    item = session.get(GroceryList, grocery_list_id)
    if not item:
        raise Exception(f'Grocery List of id {grocery_list_id} does not exist')
    return item

def create_grocery_list(session: Session, grocery_list: GroceryList) -> GroceryList:
    session.add(grocery_list)
    session.commit()
    session.refresh(grocery_list)
    return grocery_list

def update_grocery_list(session: Session, grocery_list_id: int, contents: str) -> GroceryList:
    item = get_grocery_list(session, grocery_list_id)
    item.contents = contents
    session.add(item)
    session.commit()
    return item

