from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.copilot import CopilotRequest, CopilotResponse
from services.copilot_service import generate_investigation

router = APIRouter()

@router.post("/investigate")
def investigate(request: CopilotRequest, db: Session = Depends(get_db)):
    result = generate_investigation(request.incident_id, db)
    return result