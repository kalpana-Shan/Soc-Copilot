from datetime import datetime

def check_off_hours(alert) -> tuple[int, str]:
    # Check from raw_data first, fallback to created_at
    timestamp = alert.raw_data.get("timestamp")
    if timestamp:
        try:
            hour = datetime.fromisoformat(timestamp).hour
        except:
            hour = alert.created_at.hour
    else:
        hour = alert.created_at.hour

    # Off hours = before 8AM or after 8PM
    if hour < 8 or hour >= 20:
        return 20, f"Login attempted at off-hours (hour: {hour}:00)"
    return 0, ""