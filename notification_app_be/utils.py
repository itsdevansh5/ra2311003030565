from datetime import datetime

PRIORITY = {
    "Placement": 3,
    "Result": 2,
    "Event": 1
}


def parse_time(ts):
    return datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")