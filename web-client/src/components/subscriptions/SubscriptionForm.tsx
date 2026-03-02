/** 
 * Subscription Component

Allows users:
-Add a new subscription by entering the service name, cost, and billing date
-Sends new subscription data up to the parent
Notes:
- This is an inline form
~ Osbaldo Mota
*/


import { useState } from "react"
import type { Subscription } from "../../types/Subscription"

interface Props {
  onAdd: (subscription: Subscription) => void
}

export default function SubscriptionForm({ onAdd }: Props) {
  const [name, setName] = useState("")
  const [cost, setCost] = useState("")
  const [billingDate, setBillingDate] = useState("")

    // Handles form submission
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()

    if (!name || !cost || !billingDate) return

    const newSubscription: Subscription = {
      id: Date.now(),
      name,
      cost: parseFloat(cost),
      billingDate,
    }

    onAdd(newSubscription)

    // Clears form
    setName("")
    setCost("")
    setBillingDate("")
  }

  return (
    <form
      onSubmit={handleSubmit}
      className="bg-white rounded-2xl shadow-sm border border-gray-100 p-6 mb-6 max-w-3xl"
    >
      <h3 className="text-lg font-semibold mb-4 text-gray-900">
        Add Subscription
      </h3>

      <div className="grid md:grid-cols-3 gap-4">
        <input
          type="text"
          placeholder="Service Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          className="border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-primary"
        />

        <input
          type="number"
          step="0.01"
          placeholder="Cost"
          value={cost}
          onChange={(e) => setCost(e.target.value)}
          className="border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-primary"
        />

        <input
          type="date"
          value={billingDate}
          onChange={(e) => setBillingDate(e.target.value)}
          className="border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-primary"
        />
      </div>

      <button
        type="submit"
        className="mt-4 bg-primary text-white px-4 py-2 rounded-lg hover:bg-primary-dark transition"
      >
        Add Subscription
      </button>
    </form>
  )
}