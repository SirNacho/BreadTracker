import { GroceryList } from "@/types/grocery-list"

export async function getGroceryList(listId: number) {
    const response = await fetch(`http://localhost:8000/grocery-list/${listId}`)

    const groceryList = await response.json() as GroceryList
    return groceryList
}

export async function createGroceryList(contents: string) {
    const response = await fetch('http://localhost:8000/grocery-list/create', {
        method: 'POST',
        body: JSON.stringify({ contents })
    })

    const groceryList = await response.json() as GroceryList
    return groceryList
}

export async function saveGroceryList(listId: number, contents: string) {
    const response = await fetch(`http://localhost:8000/grocery-list/save/${listId}`, {
        method: 'POST',
        body: JSON.stringify({ contents })
    })

    const groceryList = await response.json() as GroceryList
    return groceryList
}

export async function searchGroceryList(listId: number) {
    const response = await fetch(`http://localhost:8000/grocery-list/search/${listId}`, { method: 'POST' })

    const groceryList = await response.json() as GroceryList
    return groceryList
}