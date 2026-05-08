import { useState } from 'react'
import AppLayout from './components/Layout/AppLayout'
import DashboardPage from './pages/DashboardPage'
import IncidentsPage from './pages/IncidentsPage'
import CopilotPage from './pages/CopilotPage'

function App() {
  const [activePage, setActivePage] = useState('dashboard')

  const renderPage = () => {
    switch(activePage) {
      case 'dashboard':
        return <DashboardPage />
      case 'incidents':
        return <IncidentsPage />
      case 'copilot':
        return <CopilotPage />
      default:
        return <DashboardPage />
    }
  }

  return (
    <AppLayout activePage={activePage} onPageChange={setActivePage}>
      {renderPage()}
    </AppLayout>
  )
}

export default App