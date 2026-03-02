/**
 * Utility: Date Functions
 * 
 * getDaysLeft - Calculates the number of days left until the billing date.
 * Used for subscription badges
 * ~ Osbaldo Mota
 */


// Calculates days between the current date and ther billing date
export function getDaysLeft(dateString: string): number {
  const today = new Date()
  const billingDate = new Date(dateString)

  const diffTime = billingDate.getTime() - today.getTime()
  return Math.ceil(diffTime / (1000 * 60 * 60 * 24))
}