from sqlalchemy import Column, Integer, String, DateTime, JSON
from sqlalchemy.sql import func
from db.database import Base

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, index=True)        # e.g. "okta", "cloudtrail"
    user_id = Column(String, index=True)       # e.g. email or username
    ip_address = Column(String, index=True)
    event_type = Column(String, index=True)    # e.g. "login_failed"
    raw_data = Column(JSON)                    # full original payload
    created_at = Column(DateTime, default=func.now())