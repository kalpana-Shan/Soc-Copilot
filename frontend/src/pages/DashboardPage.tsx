// No import needed for React 17+

const DashboardPage: React.FC = () => {
  return (
    <div>
      <div className="bg-white rounded-lg shadow-md p-6 mb-6">
        <h2 className="text-2xl font-bold mb-2">Welcome to SOC Copilot</h2>
        <p className="text-gray-600">Your AI-powered security incident assistant.</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <div className="bg-blue-600 text-white rounded-lg p-6">
          <div className="text-3xl font-bold">0</div>
          <div className="text-sm">Active Incidents</div>
        </div>
        <div className="bg-red-600 text-white rounded-lg p-6">
          <div className="text-3xl font-bold">0</div>
          <div className="text-sm">High Risk Alerts</div>
        </div>
        <div className="bg-green-600 text-white rounded-lg p-6">
          <div className="text-3xl font-bold">0</div>
          <div className="text-sm">Resolved Today</div>
        </div>
      </div>

      <div className="bg-white rounded-lg shadow-md p-6">
        <h3 className="text-lg font-semibold mb-3">System Status</h3>
        <div className="flex justify-between py-2 border-b">
          <span>Frontend Status:</span>
          <span className="text-green-600">✅ Running</span>
        </div>
        <div className="flex justify-between py-2">
          <span>API URL:</span>
          <span className="font-mono text-sm">http://localhost:8000</span>
        </div>
      </div>
    </div>
  )
}

export default DashboardPage