from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from models.incident import Incident
from schemas.incident import IncidentRead, IncidentUpdate
from typing import List

router = APIRouter()

@router.get("/", response_model=List[IncidentRead])
def get_incidents(db: Session = Depends(get_db)):
    incidents = db.query(Incident).order_by(
        Incident.created_at.desc()
    ).all()
    return incidents

@router.get("/{incident_id}", response_model=IncidentRead)
def get_incident(incident_id: int, db: Session = Depends(get_db)):
    incident = db.query(Incident).filter(
        Incident.id == incident_id
    ).first()
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return incident

@router.patch("/{incident_id}", response_model=IncidentRead)
def update_incident_status(
    incident_id: int,
    payload: IncidentUpdate,
    db: Session = Depends(get_db)
):
    incident = db.query(Incident).filter(
        Incident.id == incident_id
    ).first()
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    
    valid_statuses = ["OPEN", "INVESTIGATING", "RESOLVED"]
    if payload.status not in valid_statuses:
        raise HTTPException(status_code=400, detail=f"Status must be one of {valid_statuses}")
    
    incident.status = payload.status
    db.commit()
    db.refresh(incident)
    return incident