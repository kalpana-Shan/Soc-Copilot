import { useState } from 'react'

const IncidentsPage: React.FC = () => {
  const [filterSeverity, setFilterSeverity] = useState('ALL')
  const [filterStatus, setFilterStatus] = useState('ALL')

  const incidents = [
    { id: 1, severity: 'HIGH', user: 'john@company.com', ip: '192.168.1.100', event: 'Failed Login', status: 'OPEN' },
    { id: 2, severity: 'MEDIUM', user: 'jane@company.com', ip: '10.0.0.45', event: 'Off-hours Login', status: 'INVESTIGATING' },
    { id: 3, severity: 'HIGH', user: 'admin@company.com', ip: '203.0.113.5', event: 'Suspicious IP', status: 'OPEN' },
  ]

  const getSeverityClass = (severity: string) => {
    switch(severity) {
      case 'HIGH': return 'bg-red-100 text-red-800'
      case 'MEDIUM': return 'bg-yellow-100 text-yellow-800'
      default: return 'bg-green-100 text-green-800'
    }
  }

  const getStatusClass = (status: string) => {
    switch(status) {
      case 'OPEN': return 'bg-red-100 text-red-800'
      case 'INVESTIGATING': return 'bg-yellow-100 text-yellow-800'
      default: return 'bg-green-100 text-green-800'
    }
  }

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Security Incidents</h2>
      
      <div className="bg-white rounded-lg shadow p-4 mb-4">
        <div className="flex gap-4">
          <select className="border rounded px-2 py-1" value={filterSeverity} onChange={(e) => setFilterSeverity(e.target.value)}>
            <option value="ALL">All Severities</option>
            <option value="HIGH">High</option>
            <option value="MEDIUM">Medium</option>
            <option value="LOW">Low</option>
          </select>
          <select className="border rounded px-2 py-1" value={filterStatus} onChange={(e) => setFilterStatus(e.target.value)}>
            <option value="ALL">All Status</option>
            <option value="OPEN">Open</option>
            <option value="INVESTIGATING">Investigating</option>
            <option value="RESOLVED">Resolved</option>
          </select>
        </div>
      </div>

      <div className="bg-white rounded-lg shadow overflow-hidden">
        <table className="w-full">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-4 py-2 text-left">ID</th>
              <th className="px-4 py-2 text-left">Severity</th>
              <th className="px-4 py-2 text-left">User</th>
              <th className="px-4 py-2 text-left">IP</th>
              <th className="px-4 py-2 text-left">Event</th>
              <th className="px-4 py-2 text-left">Status</th>
            </tr>
          </thead>
          <tbody>
            {incidents.map(incident => (
              <tr key={incident.id} className="border-t">
                <td className="px-4 py-2">{incident.id}</td>
                <td className="px-4 py-2"><span className={`px-2 py-1 rounded text-xs ${getSeverityClass(incident.severity)}`}>{incident.severity}</span></td>
                <td className="px-4 py-2">{incident.user}</td>
                <td className="px-4 py-2">{incident.ip}</td>
                <td className="px-4 py-2">{incident.event}</td>
                <td className="px-4 py-2"><span className={`px-2 py-1 rounded text-xs ${getStatusClass(incident.status)}`}>{incident.status}</span></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}

export default IncidentsPage