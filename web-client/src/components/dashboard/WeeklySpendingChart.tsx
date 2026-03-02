/**
 * WeeklySpendingChart Component
 * 
 * Displays a bar chart of weekly spending based on the user's subscriptions.
 * 
 * Notes:
 * Currently uses front-end-calculated data until we integrate backend
 * ~ Osbaldo Mota
 */


import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts"
import type { Subscription } from "../../types/Subscription"
import { generateWeeklySpending } from "../../types/utils/chartUtils"

interface Props {
  subscriptions: Subscription[]
}

export default function WeeklySpendingChart({ subscriptions }: Props) {
  const data = generateWeeklySpending(subscriptions)

  return (
    <div className="bg-white rounded-2xl shadow-sm border border-gray-100 p-6">
      <h3 className="text-lg font-semibold mb-4 text-gray-900">
        Weekly Spending
      </h3>

      <div className="h-64">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={data}>
            <XAxis dataKey="day" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="amount" fill="#059669" radius={[6, 6, 0, 0]} />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  )
}