import sys
import os
sys.path.append(os.path.abspath(".."))
from client import fetch_notifications
from service import get_top_notifications
import json


def main():
    notifications = fetch_notifications()

    if not notifications:
        print("No data fetched")
        return

    top_notifications = get_top_notifications(notifications)

    output = [
        {
            "id": n["ID"],
            "type": n["Type"],
            "message": n["Message"],
            "timestamp": n["Timestamp"]
        }
        for n in top_notifications
    ]

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()