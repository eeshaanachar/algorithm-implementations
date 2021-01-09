
def knapSack(values, weights, max_capacity):

    dp = [values[0] if weights[0] <= capacity else 0 for capacity in range(max_capacity + 1)]

    for value, weight in zip(values[1:], weights[1:]):
        for capacity in range(max_capacity, -1, -1):
            if capacity - weight >= 0:
                dp[capacity] = max(dp[capacity], dp[capacity - weight] + value)

    return dp[-1]

print(knapSack(( 25, 20, 15, 40, 50 ), ( 3, 2, 1, 4, 5 ), 6))