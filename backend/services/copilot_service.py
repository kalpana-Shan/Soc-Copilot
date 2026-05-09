from sqlalchemy.orm import Session
from models.incident import Incident
from models.alert import Alert
from fastapi import HTTPException

def generate_investigation(incident_id: int, db: Session) -> dict:
    # Fetch incident
    incident = db.query(Incident).filter(Incident.id == incident_id).first()
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")

    # Fetch linked alert
    alert = db.query(Alert).filter(Alert.id == incident.alert_id).first()
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")

    # Fetch history — last 10 alerts for same user
    history = db.query(Alert).filter(
        Alert.user_id == alert.user_id
    ).order_by(Alert.created_at.desc()).limit(10).all()

    history_count = len(history)
    last_activity = history[0].created_at if history else None

    # Build human-readable summary
    summary = (
        f"Incident #{incident.id} involves user '{alert.user_id}' "
        f"from IP {alert.ip_address}. "
        f"The system detected a {incident.severity} risk event of type "
        f"'{alert.event_type}' from source '{alert.source}'. "
        f"Risk score: {incident.risk_score}/100. "
        f"This user has {history_count} recorded alert(s) in history. "
    )

    if incident.summary:
        summary += f"Detection reason: {incident.summary}"

    # Recommended actions based on severity
    recommended_actions = []

    if incident.severity == "HIGH":
        recommended_actions = [
            "🔴 Immediately lock the user account",
            "🔴 Force password reset",
            "🔴 Revoke all active sessions",
            "🔴 Review recent access logs for data exfiltration",
            "🔴 Notify security team immediately"
        ]
    elif incident.severity == "MEDIUM":
        recommended_actions = [
            "🟡 Ask the user to verify this activity via email/phone",
            "🟡 Monitor further login attempts for next 24 hours",
            "🟡 Check if IP is associated with VPN or proxy",
            "🟡 Enable MFA if not already active"
        ]
    else:
        recommended_actions = [
            "🟢 No immediate action required",
            "🟢 Continue monitoring user activity",
            "🟢 Flag for weekly security review"
        ]

    # Update incident summary in DB
    incident.summary = summary
    db.commit()

    return {
        "incident_id": incident.id,
        "risk_score": incident.risk_score,
        "severity": incident.severity,
        "status": incident.status,
        "summary": summary,
        "recommended_actions": recommended_actions,
        "context": {
            "user_id": alert.user_id,
            "ip_address": alert.ip_address,
            "event_type": alert.event_type,
            "source": alert.source,
            "history_count": history_count,
            "last_activity": last_activity.isoformat() if last_activity else None
        }
    }