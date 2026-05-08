// No import needed - remove the line or keep if using React.ReactNode

interface AppLayoutProps {
  children: React.ReactNode
  activePage: string
  onPageChange: (page: string) => void
}

const AppLayout: React.FC<AppLayoutProps> = ({ children, activePage, onPageChange }) => {
  const menuItems = [
    { id: 'dashboard', label: 'Dashboard', icon: '📊' },
    { id: 'incidents', label: 'Incidents', icon: '⚠️' },
    { id: 'copilot', label: 'Copilot', icon: '🤖' },
  ]

  return (
    <div className="flex min-h-screen bg-gray-50">
      {/* Sidebar */}
      <aside className="w-64 bg-gray-900 text-white">
        <div className="p-6">
          <h2 className="text-xl font-bold mb-6">SOC Copilot</h2>
          <nav className="space-y-2">
            {menuItems.map((item) => (
              <button
                key={item.id}
                onClick={() => onPageChange(item.id)}
                className={`w-full text-left px-4 py-3 rounded-lg flex items-center gap-3 ${
                  activePage === item.id ? 'bg-blue-600' : 'hover:bg-gray-800'
                }`}
              >
                <span className="text-xl">{item.icon}</span>
                <span>{item.label}</span>
              </button>
            ))}
          </nav>
        </div>
      </aside>

      {/* Main Content */}
      <div className="flex-1">
        <header className="bg-white border-b px-8 py-4">
          <h1 className="text-2xl font-bold text-gray-900 capitalize">{activePage}</h1>
        </header>
        <main className="p-8">
          {children}
        </main>
      </div>
    </div>
  )
}

export default AppLayout