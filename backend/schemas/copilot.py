from pydantic import BaseModel
from typing import List, Optional

class CopilotRequest(BaseModel):
    incident_id: int

class CopilotContext(BaseModel):
    user_id: str
    ip_address: str
    event_type: str
    history_count: int
    last_activity: Optional[str] = None

class CopilotResponse(BaseModel):
    incident_id: int
    risk_score: int
    severity: str
    summary: str
    recommended_actions: List[str]
    context: CopilotContext