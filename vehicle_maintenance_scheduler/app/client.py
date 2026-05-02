import requests
from logging_middleware import Log
import os

BASE_URL = "http://20.207.122.201/evaluation-service"

def get_headers():
    token = os.getenv("AUTH_TOKEN")
    
    if not token:
        raise Exception("AUTH_TOKEN not set in environment")

    return {
        "Authorization": f"Bearer {token}"
    }


def fetch_depots():
    try:
        headers = get_headers()

        res = requests.get(f"{BASE_URL}/depots", headers=headers)

        if res.status_code != 200:
            Log("backend", "error", "service", f"Depot API failed: {res.status_code}")
            return []

        data = res.json()

        Log("backend", "info", "service", "Fetched depots")
        return data.get("depots", [])

    except Exception as e:
        Log("backend", "error", "service", f"Depot fetch failed: {e}")
        return []


def fetch_vehicles():
    try:
        headers = get_headers()

        res = requests.get(f"{BASE_URL}/vehicles", headers=headers)

        if res.status_code != 200:
            Log("backend", "error", "service", f"Vehicle API failed: {res.status_code}")
            return []

        data = res.json()

        Log("backend", "info", "service", "Fetched vehicles")
        return data.get("vehicles", [])

    except Exception as e:
        Log("backend", "error", "service", f"Vehicle fetch failed: {e}")
        return []