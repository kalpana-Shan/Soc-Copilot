from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.sql import func
from db.database import Base

class ActionLog(Base):
    __tablename__ = "action_logs"

    id = Column(Integer, primary_key=True, index=True)
    incident_id = Column(Integer, ForeignKey("incidents.id"))
    action_type = Column(String)               # "BLOCK_IP", "RESET_PASSWORD", "MONITOR"
    performed_by = Column(String)              # analyst name or "system"
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=func.now())