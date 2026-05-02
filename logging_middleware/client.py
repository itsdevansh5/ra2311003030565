import requests
import os

LOG_API_URL = "http://20.207.122.201/evaluation-service/logs"

def get_headers():
    token = os.getenv("AUTH_TOKEN")
    if not token:
        return None
    return {
        "Authorization": f"Bearer {token}"
    }

def send_log(payload):
    try:
        headers = get_headers()
        if not headers:
            return  

        res=requests.post(LOG_API_URL, json=payload, headers=headers, timeout=5)
        print("LOG STATUS:", res.status_code)

    except:
        pass  