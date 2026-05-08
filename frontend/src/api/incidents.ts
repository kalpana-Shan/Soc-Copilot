import api from './client'

export interface Incident {
  id: number
  alert_id: number
  severity: 'HIGH' | 'MEDIUM' | 'LOW'
  status: 'OPEN' | 'INVESTIGATING' | 'RESOLVED'
  risk_score: number
  summary: string | null
  created_at: string
  updated_at?: string
  alert?: {
    source: string
    user_id: string
    ip_address: string
    event_type: string
    raw_data: any
  }
}

export interface CopilotResponse {
  incident_id: number
  risk_score: number
  severity: string
  summary: string
  recommended_actions: string[]
  context: {
    user_id: string
    ip_address: string
    event_type: string
    last_activity: string | null
    history_count: number
  }
}

// Fetch all incidents
export const fetchIncidents = async (): Promise<Incident[]> => {
  try {
    const response = await api.get('/incidents')
    return response.data
  } catch (error) {
    console.error('Failed to fetch incidents:', error)
    // Return mock data for demo if backend is not available
    return getMockIncidents()
  }
}

// Fetch single incident by ID
export const fetchIncidentById = async (id: number): Promise<Incident> => {
  try {
    const response = await api.get(`/incidents/${id}`)
    return response.data
  } catch (error) {
    console.error(`Failed to fetch incident ${id}:`, error)
    throw error
  }
}

// Update incident status
export const updateIncidentStatus = async (id: number, status: string): Promise<Incident> => {
  try {
    const response = await api.patch(`/incidents/${id}`, { status })
    return response.data
  } catch (error) {
    console.error(`Failed to update incident ${id}:`, error)
    throw error
  }
}

// Ask Copilot about an incident
export const askCopilot = async (incidentId: number): Promise<CopilotResponse> => {
  try {
    const response = await api.post('/copilot/investigate', { incident_id: incidentId })
    return response.data
  } catch (error) {
    console.error(`Failed to get Copilot response for incident ${incidentId}:`, error)
    // Return mock response if backend is not available
    return getMockCopilotResponse(incidentId)
  }
}

// Mock data for when backend is not available
const getMockIncidents = (): Incident[] => {
  return [
    {
      id: 1,
      alert_id: 101,
      severity: 'HIGH',
      status: 'OPEN',
      risk_score: 85,
      summary: 'Multiple failed login attempts',
      created_at: new Date().toISOString(),
      alert: {
        source: 'okta',
        user_id: 'john.doe@company.com',
        ip_address: '192.168.1.100',
        event_type: 'login_failed',
        raw_data: {}
      }
    },
    {
      id: 2,
      alert_id: 102,
      severity: 'MEDIUM',
      status: 'INVESTIGATING',
      risk_score: 55,
      summary: 'Off-hours login detected',
      created_at: new Date().toISOString(),
      alert: {
        source: 'azure',
        user_id: 'jane.smith@company.com',
        ip_address: '10.0.0.45',
        event_type: 'off_hours_login',
        raw_data: {}
      }
    },
    {
      id: 3,
      alert_id: 103,
      severity: 'HIGH',
      status: 'OPEN',
      risk_score: 90,
      summary: 'Suspicious IP access',
      created_at: new Date().toISOString(),
      alert: {
        source: 'cloudflare',
        user_id: 'admin@company.com',
        ip_address: '203.0.113.5',
        event_type: 'suspicious_ip',
        raw_data: {}
      }
    }
  ]
}

const getMockCopilotResponse = (incidentId: number): CopilotResponse => {
  return {
    incident_id: incidentId,
    risk_score: 85,
    severity: 'HIGH',
    summary: `Incident ${incidentId} involves suspicious activity detected from IP address. Multiple indicators of compromise identified.`,
    recommended_actions: [
      'Immediately lock the user account',
      'Force password reset',
      'Review recent access logs',
      'Check for unusual activity in the last 24 hours'
    ],
    context: {
      user_id: 'user@company.com',
      ip_address: '192.168.1.100',
      event_type: 'suspicious_login',
      last_activity: new Date().toISOString(),
      history_count: 3
    }
  }
}