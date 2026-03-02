/*
Main App component 

Resposnible for:
- Managing the state of subscriptions
- Handling tab switching (Dashboard / Subscriptions)
- Persisting subscription data using localStorage

Notes:
- All subscription data is stored in localStorage right now until we integrate with a backend API

~ Osbaldo Mota
*/

import { useState, useEffect } from "react"
import Layout from "./components/layout/Layout"
import Navbar from "./components/layout/Navbar"
import Card from "./components/ui/Card"
import SubscriptionList from "./components/subscriptions/SubscriptionList"
import type { Subscription } from "./types/Subscription"
import WeeklySpendingChart from "./components/dashboard/WeeklySpendingChart"
import UpcomingCharges from "./components/dashboard/UpcomingCharges"
import {
  calculateMonthlyExpenses,
  calculateActiveSubscriptions,
  calculateUpcomingChargesTotal,
} from "./types/utils/financialUtils"


export default function App() {
  const [subscriptions, setSubscriptions] = useState<Subscription[]>([])

  // The actuive tab states which controls Dashboard vs Subscriptions view
  const [activeTab, setActiveTab] = useState<"dashboard" | "subscriptions">("dashboard")
  // Subsscription state
  // Adds a new subscription to the list
  const handleAdd = (newSubscription: Subscription) => {
  setSubscriptions((prev) => [...prev, newSubscription])
}

  
const [hasLoaded, setHasLoaded] = useState(false)

// Load subscriptions from localStorage on app start
useEffect(() => {
  const saved = localStorage.getItem("subscriptions")
  if (saved) {
    try {
      setSubscriptions(JSON.parse(saved))
    } catch (error) {
      console.error("Failed to parse subscriptions from localStorage", error)
    }
  }
  // Mark that loading is complete
  setHasLoaded(true)
}, [])

// Save to localStorage ONLY after initial load is done
useEffect(() => {
  if (!hasLoaded) return
  localStorage.setItem("subscriptions", JSON.stringify(subscriptions))
}, [subscriptions, hasLoaded])
// Deletes a subscription by id
  const handleDelete = (id: number) => {
    setSubscriptions((prev) => prev.filter((sub) => sub.id !== id))
  }

  // Dynamic dashboard metrics based on subscription data
  const monthlyExpenses = calculateMonthlyExpenses(subscriptions)
  const activeSubscriptions = calculateActiveSubscriptions(subscriptions)
  const upcomingChargesTotal = calculateUpcomingChargesTotal(subscriptions)

  return (
    <>
      <Navbar activeTab={activeTab} setActiveTab={setActiveTab} />

      <Layout>
        {activeTab === "dashboard" && (
          <>
            <div className="mb-8">
              <h2 className="text-2xl font-semibold text-gray-900">
                Dashboard Overview
              </h2>
              <p className="text-gray-500 text-sm mt-1">
                Here’s a summary of your financial activity.
              </p>
            </div>
            <div className="grid md:grid-cols-3 gap-6">
            <Card
             title="Monthly Subscription Cost"
             value={`$${monthlyExpenses.toFixed(2)}`}
              />

            <Card
              title="Active Subscriptions"
              value={`${activeSubscriptions}`}
            />

            <Card
              title="Upcoming Charges"
              value={`$${upcomingChargesTotal.toFixed(2)}`}
            />
          </div>
            
            <div className="mt-10 grid lg:grid-cols-3 gap-6">
            <div className="lg:col-span-2">
            <WeeklySpendingChart subscriptions={subscriptions} />
            </div>

          <UpcomingCharges subscriptions={subscriptions} />
          </div>
          </>
        )}

        {activeTab === "subscriptions" && (
          <SubscriptionList
            subscriptions={subscriptions}
            onDelete={handleDelete}
            onAdd={handleAdd}
          />
        )}
      </Layout>
    </>
  )
}
