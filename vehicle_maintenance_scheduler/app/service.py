from logging_middleware import Log

def knapsack(vehicles, capacity):
    n = len(vehicles)
    dp = [[0]*(capacity+1) for _ in range(n+1)]

    for i in range(1, n+1):
        dur = vehicles[i-1]["Duration"]
        imp = vehicles[i-1]["Impact"]

        for w in range(capacity+1):
            if dur <= w:
                dp[i][w] = max(
                    imp + dp[i-1][w-dur],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]

    return dp


def get_selected(dp, vehicles, capacity):
    res = []
    i = len(vehicles)
    w = capacity

    while i > 0:
        if dp[i][w] != dp[i-1][w]:
            res.append(vehicles[i-1])
            w -= vehicles[i-1]["Duration"]
        i -= 1

    return res


def schedule_for_depot(vehicles, capacity):
    Log("backend", "debug", "service", f"Running knapsack for capacity {capacity}")

    dp = knapsack(vehicles, capacity)
    selected = get_selected(dp, vehicles, capacity)

    Log("backend", "info", "service", f"Selected {len(selected)} vehicles")

    return selected