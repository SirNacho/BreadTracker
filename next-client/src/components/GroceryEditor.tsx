'use client'

import { useState } from "react"
import { GroceryList } from "@/types/grocery-list";
import { saveGroceryList } from "@/utils/grocery-list";
import { Button } from "./ui/button";

type Props = {
    groceryList: GroceryList
}

export function GroceryEditor({ groceryList }: Props) {
    const [contents, setContents] = useState(groceryList.contents)
    
    return (
        <div className="flex flex-col gap-y-4">
            <textarea
                value={contents}
                onChange={e => setContents(e.target.value)}
                className="text-white text-2xl w-full rounded-2xl bg-slate-800 outline-0 p-4 resize-none"
                rows={16}
            />
            <div className="flex items-center justify-end gap-x-4">
                <Button
                    className="text-lg text-white bg-green-800 px-8 py-1 rounded-full hover:ring-2 hover:ring-white transition-all duration-300 cursor-pointer"
                    onClick={() => saveGroceryList(groceryList.groceryListId, contents)}
                >
                    Save
                </Button>
                <Button 
                    className="text-lg text-white bg-green-800 px-8 py-1 rounded-full hover:ring-2 hover:ring-white transition-all duration-300 cursor-pointer"
                >
                    Search
                </Button>
            </div>
        </div>
    )
}