export type GroceryOption = {
    title: string
    price: string
    store: string
    thumbnail: string
}

export type GroceryList = {
    groceryListId: number
    contents: string
    groceryOptions: unknown
    createdAt: Date
    modifiedAt: Date
}