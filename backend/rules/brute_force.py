def check_brute_force(alert) -> tuple[int, str]:
    failed_count = alert.raw_data.get("failed_count", 0)
    if failed_count >= 10:
        return 50, f"Severe brute force: {failed_count} failed login attempts"
    elif failed_count >= 5:
        return 40, f"Multiple failed logins: {failed_count} attempts"
    elif alert.event_type == "login_failed":
        return 10, "Single failed login attempt"
    return 0, ""