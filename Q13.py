def knapsack_dynamic(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w - weights[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]

weights = [10, 20, 30, 15, 35]
values = [60, 100, 120, 50, 180]
capacity = 50

result = knapsack_dynamic(weights, values, capacity)
print(f"O valor máximo que pode ser colocado na mochila é: {result}")