/** 
SubscriptionList Component

Displays:
-List of current subscriptions
-Days remaing untill next payment
-Delete button
-Dyanmic button (red, yellow, green) based on how close the billing date is

~ Osbaldo Mota
*/

import type { Subscription } from "../../types/Subscription"
import { getDaysLeft } from "../../types/utils/dateUtils"
import SubscriptionForm from "./SubscriptionForm"

interface Props {
  subscriptions: Subscription[]
  onDelete: (id: number) => void
  onAdd: (subscription: Subscription) => void
}

export default function SubscriptionList({
  subscriptions,
  onDelete,
  onAdd,
}: Props) {
  // Returns color class based on how close the billing date is
    const getBadgeColor = (days: number) => {
  if (days <= 2) return "bg-red-100 text-red-700"
  if (days <= 7) return "bg-yellow-100 text-yellow-700"
  return "bg-emerald-100 text-emerald-700"
}
  return (
    <div>
      <SubscriptionForm onAdd={onAdd} />
    
    <div className="bg-white rounded-2xl shadow-sm border border-gray-100 p-6 max-w-3xl">
      <h2 className="text-xl font-semibold mb-6 text-gray-900">
        Subscriptions
      </h2>

      {subscriptions.length === 0 ? (
        <p className="text-gray-500 text-sm">
          No subscriptions added yet.
        </p>
      ) : (

        // Renders each subscription with name, cost, billing date, days left badge, and delete button
        <div className="space-y-4">
          {subscriptions.map((sub) => {
            const daysLeft = getDaysLeft(sub.billingDate)

            return (
              <div
                key={sub.id}
                className="flex justify-between items-center p-4 border rounded-xl bg-gray-50"
              >
                <div>
                  <p className="font-medium text-gray-900">
                    {sub.name}
                  </p>
                  <p className="text-sm text-gray-500">
                    ${sub.cost} • Due: {sub.billingDate}
                  </p>
                </div>

                <div className="flex items-center gap-4">
                  <span
                    className={`px-3 py-1 text-xs font-semibold rounded-full ${getBadgeColor(daysLeft)}`}
                    >
                    {daysLeft} days left
                    </span>

                  <button
                    onClick={() => onDelete(sub.id)}
                    className="text-red-500 hover:text-red-600 text-sm font-medium"
                  >
                    Delete
                  </button>
                </div>
              </div>
            )
          })}
        </div>
      )}
    </div>
    </div>
  )
}