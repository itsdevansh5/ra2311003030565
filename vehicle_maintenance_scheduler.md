# Vehicle Maintenance Scheduler

## Approach
- Modeled problem as 0/1 Knapsack
- Duration = weight
- Impact = value
- MechanicHours = capacity

## Features
- Fetches data from APIs with authentication
- Reusable logging middleware
- Validates constraints (duration ≤ capacity)
- Clean JSON output

## Logging
- Centralized logging module
- Token-based authentication
- Non-blocking logging (fail-safe)

## Tech Stack
- Python
- Requests