from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any

class AlertCreate(BaseModel):
    source: str           # "okta", "cloudtrail", "azure_ad"
    user_id: str          # email or username
    ip_address: str
    event_type: str       # "login_failed", "suspicious_login"
    raw_data: Dict[str, Any]  # full original payload

class AlertRead(BaseModel):
    id: int
    source: str
    user_id: str
    ip_address: str
    event_type: str
    raw_data: Dict[str, Any]
    created_at: datetime

    model_config = {"from_attributes": True}