from app.client import fetch_depots, fetch_vehicles
from app.service import schedule_for_depot
from logging_middleware import Log

def main():
    depots = fetch_depots()
    vehicles = fetch_vehicles()

    results = []

    for depot in depots:
        depot_id = depot["ID"]
        capacity = depot["MechanicHours"]

        Log("backend", "info", "service", f"Processing depot {depot_id}")

        selected = schedule_for_depot(vehicles, capacity)

        results.append({
            "depotId": depot_id,
            "selectedVehicles": [v["TaskID"] for v in selected]
        })

    print(results)


if __name__ == "__main__":
    main()