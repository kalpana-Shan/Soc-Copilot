from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class IncidentRead(BaseModel):
    id: int
    alert_id: int
    severity: str         # "LOW", "MEDIUM", "HIGH"
    status: str           # "OPEN", "INVESTIGATING", "RESOLVED"
    risk_score: int
    summary: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}

class IncidentUpdate(BaseModel):
    status: str           # "OPEN", "INVESTIGATING", "RESOLVED"