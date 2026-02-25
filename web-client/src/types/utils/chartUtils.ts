import type { Subscription } from "../Subscription"

// Define strict weekday type
type WeekDay = "Sun" | "Mon" | "Tue" | "Wed" | "Thu" | "Fri" | "Sat"

const daysOfWeek: WeekDay[] = [
  "Sun",
  "Mon",
  "Tue",
  "Wed",
  "Thu",
  "Fri",
  "Sat",
]

export function generateWeeklySpending(subscriptions: Subscription[]) {
  // Properly typed record
  const weeklyData: Record<WeekDay, number> = {
    Sun: 0,
    Mon: 0,
    Tue: 0,
    Wed: 0,
    Thu: 0,
    Fri: 0,
    Sat: 0,
  }

  subscriptions.forEach((sub) => {
    const date = new Date(sub.billingDate)
    const dayName = daysOfWeek[date.getDay()] // Now typed as WeekDay
    weeklyData[dayName] += sub.cost
  })

  return daysOfWeek.map((day) => ({
    day,
    amount: Number(weeklyData[day].toFixed(2)),
  }))
}