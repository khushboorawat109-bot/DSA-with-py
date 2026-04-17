
import math

def tsp_dp(cost):
    n = len(cost)
    dp = [[math.inf] * n for _ in range(1 << n)]
    
    # Starting from city 0
    dp[1][0] = 0

    for mask in range(1 << n):
        for u in range(n):
            if mask & (1 << u):  # if u is in mask
                for v in range(n):
                    if not (mask & (1 << v)):  # if v not visited
                        new_mask = mask | (1 << v)
                        dp[new_mask][v] = min(
                            dp[new_mask][v],
                            dp[mask][u] + cost[u][v]
                        )

    # Return to starting city
    ans = math.inf
    for i in range(n):
        ans = min(ans, dp[(1 << n) - 1][i] + cost[i][0])

    return ans


# Example
cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

print("Minimum cost:", tsp_dp(cost))

