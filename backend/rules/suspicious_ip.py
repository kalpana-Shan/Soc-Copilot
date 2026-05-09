import json
import os

# Load blocklist from data folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOCKLIST_PATH = os.path.join(BASE_DIR, "data", "blocklist_ips.json")

def load_blocklist():
    try:
        with open(BLOCKLIST_PATH) as f:
            return json.load(f).get("blocked_ips", [])
    except:
        return []

BLOCKED_IPS = load_blocklist()

def check_suspicious_ip(alert) -> tuple[int, str]:
    if alert.ip_address in BLOCKED_IPS:
        return 30, f"IP {alert.ip_address} is in the blocklist"
    return 0, ""