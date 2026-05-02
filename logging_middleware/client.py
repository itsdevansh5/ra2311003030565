import requests

LOG_API_URL = "http://20.207.122.201/evaluation-service/logs"

def send_log(data):
    try:
        response = requests.post(LOG_API_URL, json=data, timeout=2)
        return response.status_code
    except Exception as e:
        print("Log API failed:", e)