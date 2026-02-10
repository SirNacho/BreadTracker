import { GroceryOption } from "@/types/grocery-list"

type Props = { searchParams: Promise<{ data?: string }> }

export default async function StoreIdPage({ searchParams }: Props) {
    const {data} = await searchParams
    const store: GroceryOption[] | undefined = data ? JSON.parse(data) : undefined

    if (!store) return null
    return (
        <div className="bg-black h-screen flex flex-col gap-y-4 items-center justify-center">
            <h1 className="text-3xl font-bold text-white">{store[0].store}</h1>
            <h2 className="text-2xl font-bold text-white">{store[0].price}</h2>
        </div>
    )
}
