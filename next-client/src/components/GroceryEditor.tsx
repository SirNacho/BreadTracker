'use client'

import { useState, useTransition } from 'react'
import { GroceryList } from '@/types/grocery-list'
import { saveGroceryList, searchGroceryList, selectSku } from '@/utils/grocery-list'
import { Button } from './ui/button'
import { Loader2 } from 'lucide-react'
import { useRouter } from 'next/navigation'
import Image from 'next/image'
import classnames from 'classnames'

type Props = { initGroceryList: GroceryList }

export function GroceryEditor({ initGroceryList }: Props) {
  const router = useRouter()
  const [groceryList, setGroceryList] = useState(initGroceryList)
  const [contents, setContents] = useState(initGroceryList.contents)
  const [selections, setSelections] = useState<Record<string, string>>({})
  const [isPending, startTransition] = useTransition()

  const handleSearch = async () => {
    startTransition(async () => {
      const list = await searchGroceryList(groceryList.groceryListId)
      setGroceryList(list)
    })
  }

  const handleSelectCategory = (grocery: string, category: string) => {
    setSelections(prev => ({ ...prev, [grocery]: category }))
  }

  const handleFindCheapestStore = async () => {
    startTransition(async () => {
      try {
        console.log(selections)
        const data = await selectSku(groceryList.groceryListId, selections)
        const encodedData = encodeURIComponent(JSON.stringify(data))
        router.push(`/store?data=${encodedData}`)
      } catch (error) {
        console.error(error)
      }
    })
  }

  return (
    <div className="flex gap-x-4">
      <div className="flex flex-col gap-y-4 flex-1">
        <textarea
          value={contents}
          onChange={(e) => setContents(e.target.value)}
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
            onClick={() => handleSearch()}
            disabled={isPending}
          >
            {isPending ? <Loader2 className="animate-spin" /> : "Search"}
          </Button>
        </div>
      </div>
      {groceryList.groceryOptions ? (
        <div className="p-4 bg-slate-800 text-white rounded-2xl flex flex-col gap-y-4">
          {Object.entries(groceryList.groceryOptions).map(([grocery, categories], i) => (
            <div key={i} className='flex flex-col'>
              <label className="text-xl font-bold">{grocery}</label>
              {Object.entries(categories).map(([category, items], j) => (
                <button 
                    key={j}
                    onClick={() => handleSelectCategory(grocery, category)} 
                    className={classnames(
                        "p-2 flex gap-x-2 items-center hover:bg-slate-600 transition-all duration-300 rounded-2xl cursor-pointer", 
                        {'ring-2 ring-white': selections[grocery] === category})
                    }
                >
                  <Image
                    src={items[0].thumbnail}
                    alt={category}
                    height={48}
                    width={100}
                    className="h-20 w-auto rounded-lg object-contain"
                  />
                  {category}
                </button>
              ))}
            </div>
          ))}
          <Button
            onClick={() => handleFindCheapestStore()} 
            className="text-lg text-white bg-green-800 px-8 py-1 rounded-full hover:ring-2 hover:ring-white transition-all duration-300 cursor-pointer"
          >
            Find cheapest store
          </Button>
        </div>
      ) : null}
    </div>
  )
}