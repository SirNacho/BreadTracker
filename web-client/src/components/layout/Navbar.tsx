import logo from "../../assets/logo.png"

interface NavbarProps {
  activeTab: "dashboard" | "subscriptions"
  setActiveTab: (tab: "dashboard" | "subscriptions") => void
}

export default function Navbar({ activeTab, setActiveTab }: NavbarProps) {
  const tabClass = (tab: string) =>
    `cursor-pointer transition ${
      activeTab === tab
        ? "text-primary font-semibold"
        : "text-gray-600 hover:text-primary"
    }`

  return (
    <nav className="bg-card shadow-sm border-b border-gray-200">
      <div className="max-w-6xl mx-auto px-6 py-4 flex justify-between items-center">
        <div className="flex items-center gap-3">
        <img
          src={logo}
          alt="BreadTracker Logo"
          className="w-14 h-14 object-contain"
        />
        <h1 className="text-xl font-semibold text-primary">
          BreadTracker
        </h1>
      </div>

        <div className="flex gap-8 text-sm font-medium">
          <button
            className={tabClass("dashboard")}
            onClick={() => setActiveTab("dashboard")}
          >
            Dashboard
          </button>

          <button
            className={tabClass("subscriptions")}
            onClick={() => setActiveTab("subscriptions")}
          >
            Subscriptions
          </button>
        </div>
      </div>
    </nav>
  )
}