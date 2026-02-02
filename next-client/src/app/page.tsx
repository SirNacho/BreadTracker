import { GroceryEditor } from "@/components/GroceryEditor";
import { getGroceryList } from "@/utils/grocery-list";

export default async function Home() {
  const groceryListId = 1
  const groceryList = await getGroceryList(groceryListId)

  return (
    <div className="p-16 bg-black h-screen">
        <GroceryEditor groceryList={groceryList} />
    </div>
  );
}
