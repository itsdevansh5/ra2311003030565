import requests
from logging_middleware import Log

BASE_URL = "http://20.207.122.201/evaluation-service"

def fetch_depots():
    try:
        res = requests.get(f"{BASE_URL}/depots")
        data = res.json()
        Log("backend", "info", "service", "Fetched depots")
        return data.get("depots", [])
    except Exception as e:
        Log("backend", "error", "service", f"Depot fetch failed: {e}")
        return []

def fetch_vehicles():
    try:
        res = requests.get(f"{BASE_URL}/vehicles")
        data = res.json()
        Log("backend", "info", "service", "Fetched vehicles")
        return data.get("vehicles", [])
    except Exception as e:
        Log("backend", "error", "service", f"Vehicle fetch failed: {e}")
        return []