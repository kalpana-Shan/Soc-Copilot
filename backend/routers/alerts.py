from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from models.alert import Alert
from schemas.alert import AlertCreate, AlertRead
from services.detection_engine import run_detection
from typing import List

router = APIRouter()

@router.post("/ingest", response_model=AlertRead)
def ingest_alert(alert: AlertCreate, db: Session = Depends(get_db)):
    # Save alert
    new_alert = Alert(
        source=alert.source,
        user_id=alert.user_id,
        ip_address=alert.ip_address,
        event_type=alert.event_type,
        raw_data=alert.raw_data
    )
    db.add(new_alert)
    db.commit()
    db.refresh(new_alert)

    # Run detection engine → auto create incident
    run_detection(new_alert, db)

    return new_alert

@router.get("/", response_model=List[AlertRead])
def get_alerts(db: Session = Depends(get_db)):
    alerts = db.query(Alert).order_by(Alert.created_at.desc()).all()
    return alerts