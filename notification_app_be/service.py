from utils import PRIORITY, parse_time
from logging_middleware import Log


def get_top_notifications(notifications, k=10):
    try:
        sorted_data = sorted(
            notifications,
            key=lambda x: (
                PRIORITY.get(x["Type"], 0),
                parse_time(x["Timestamp"])
            ),
            reverse=True
        )

        top_k = sorted_data[:k]

        Log("backend", "info", "service", f"Selected top {k} notifications")

        return top_k

    except Exception as e:
        Log("backend", "error", "service", f"Sorting failed: {e}")
        return []