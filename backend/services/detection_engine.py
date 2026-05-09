from sqlalchemy.orm import Session
from models.alert import Alert
from models.incident import Incident
from services.risk_scorer import calculate_risk_score
from typing import Optional

def run_detection(alert: Alert, db: Session) -> Optional[Incident]:
    score, severity, reasons = calculate_risk_score(alert)

    # Only create incident if score >= 30
    if score < 30:
        print(f"Alert {alert.id} scored {score} — too low, no incident created.")
        return None

    summary = f"Suspicious activity detected for user {alert.user_id}. " \
              f"Reasons: {'; '.join(reasons)}"

    incident = Incident(
        alert_id=alert.id,
        severity=severity,
        status="OPEN",
        risk_score=score,
        summary=summary
    )
    db.add(incident)
    db.commit()
    db.refresh(incident)
    print(f"✅ Incident created: ID={incident.id}, Severity={severity}, Score={score}")
    return incident