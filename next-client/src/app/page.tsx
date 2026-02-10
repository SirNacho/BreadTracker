import { GroceryEditor } from "@/components/GroceryEditor";
import { fetchGroceryList } from "@/utils/grocery-list";

export default async function Home() {
  const groceryListId = 1
  const groceryList = await fetchGroceryList(groceryListId)

  return (
    <div className="p-16 bg-black min-h-screen">
        <GroceryEditor initGroceryList={groceryList} />
    </div>
  );
}
