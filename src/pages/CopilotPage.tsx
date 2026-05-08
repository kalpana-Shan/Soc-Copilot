import { useState } from 'react'

const CopilotPage: React.FC = () => {
  const [incidentId, setIncidentId] = useState('')
  const [response, setResponse] = useState('')
  const [loading, setLoading] = useState(false)

  const handleInvestigate = () => {
    if (!incidentId) {
      alert('Please enter an incident ID')
      return
    }
    
    setLoading(true)
    setTimeout(() => {
      setResponse(`## Incident #${incidentId} Analysis\n\n**Risk Score:** 85/100 (HIGH)\n\n**Summary:** Multiple failed login attempts detected from suspicious IP address.\n\n**Recommended Actions:**\n1. Lock the user account\n2. Force password reset\n3. Review access logs`)
      setLoading(false)
    }, 1500)
  }

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">SOC Copilot Assistant</h2>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-lg font-semibold mb-4">Investigate Incident</h3>
          <input
            type="number"
            placeholder="Enter Incident ID"
            className="w-full border rounded px-3 py-2 mb-4"
            value={incidentId}
            onChange={(e) => setIncidentId(e.target.value)}
          />
          <button
            onClick={handleInvestigate}
            disabled={loading}
            className="w-full bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
          >
            {loading ? 'Investigating...' : 'Ask Copilot'}
          </button>
        </div>

        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-lg font-semibold mb-4">Investigation Results</h3>
          <div className="bg-gray-50 rounded p-4 min-h-[300px] whitespace-pre-wrap">
            {response || 'Enter an incident ID and click "Ask Copilot" to start investigation.'}
          </div>
        </div>
      </div>
    </div>
  )
}

export default CopilotPage