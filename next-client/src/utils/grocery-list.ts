import { GroceryList, GroceryOption } from "@/types/grocery-list"

export async function fetchGroceryList(listId: number) {
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

export async function selectSku(listId: number, selections: Record<string, string>) {
    const response = await fetch(`http://localhost:8000/grocery-list/select-skus/${listId}`, {
        method: 'POST',
        body: JSON.stringify(selections),
        headers: { 'Content-Type': 'application/json' }
    })

    const groceries = await response.json() as GroceryOption
    return groceries

}