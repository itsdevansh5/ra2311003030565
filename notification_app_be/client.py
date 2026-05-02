import requests
import os
from dotenv import load_dotenv
from logging_middleware import Log

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")


def fetch_notifications():
    try:
        headers = {
            "Authorization": f"Bearer {AUTH_TOKEN}"
        }

        res = requests.get(f"{BASE_URL}/notifications", headers=headers, timeout=5)
        res.raise_for_status()

        data = res.json()
        Log("backend", "info", "service", "Fetched notifications")

        return data.get("notifications", [])

    except Exception as e:
        Log("backend", "error", "service", f"Fetch failed: {e}")
        return []