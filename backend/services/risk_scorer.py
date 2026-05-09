from rules.brute_force import check_brute_force
from rules.off_hours_access import check_off_hours
from rules.suspicious_ip import check_suspicious_ip

def calculate_risk_score(alert) -> tuple[int, str, list[str]]:
    total_score = 0
    reasons = []

    # Run all rules
    score, reason = check_brute_force(alert)
    if score > 0:
        total_score += score
        reasons.append(reason)

    score, reason = check_off_hours(alert)
    if score > 0:
        total_score += score
        reasons.append(reason)

    score, reason = check_suspicious_ip(alert)
    if score > 0:
        total_score += score
        reasons.append(reason)

    # Cap at 100
    total_score = min(total_score, 100)

    # Map to severity
    if total_score >= 80:
        severity = "HIGH"
    elif total_score >= 50:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    return total_score, severity, reasons