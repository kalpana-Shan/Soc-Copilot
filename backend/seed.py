import requests
import json
import os

BASE_URL = "http://localhost:8000"

def seed_alerts():
    # Load sample alerts
    data_path = os.path.join(os.path.dirname(__file__), "data", "sample_alerts.json")
    with open(data_path) as f:
        data = json.load(f)

    print("🌱 Seeding demo alerts...\n")

    for i, alert in enumerate(data["alerts"], 1):
        response = requests.post(f"{BASE_URL}/alerts/ingest", json=alert)
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Alert {i} ingested: ID={result['id']} | {alert['event_type']} | {alert['user_id']}")
        else:
            print(f"❌ Alert {i} failed: {response.text}")

    print("\n📊 Checking incidents created...")
    incidents = requests.get(f"{BASE_URL}/incidents/").json()
    print(f"✅ Total incidents created: {len(incidents)}")
    for inc in incidents:
        print(f"   → Incident {inc['id']}: {inc['severity']} | Score: {inc['risk_score']} | Status: {inc['status']}")

if __name__ == "__main__":
    seed_alerts()