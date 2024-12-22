"""
Dynamic programming solution -> O(N*W)
"""


def knapsack(condition_weight, weights, values, no_of_vals):
    dp = [[0 for _ in range(condition_weight + 1)] for _ in range(no_of_vals + 1)]

    # Build table K[][] in bottom up manner
    for no_of_val in range(no_of_vals + 1):
        for w in range(condition_weight + 1):
            if no_of_val == 0 or w == 0:
                dp[no_of_val][w] = 0
            elif weights[no_of_val - 1] <= w:
                dp[no_of_val][w] = max(
                    values[no_of_val - 1] + dp[no_of_val - 1][w - weights[no_of_val - 1]],
                    dp[no_of_val - 1][w],
                )
            else:
                dp[no_of_val][w] = dp[no_of_val - 1][w]

    return dp[no_of_vals][condition_weight]


def knapsack_test(condition_weight, weights, values, no_of_vals):
    dp = [[0 for _ in range(condition_weight + 1)] for _ in range(no_of_vals + 1)]

    for no_of_val in range(no_of_vals + 1):
        for w in range(weights + 1):
            if no_of_val == 0 or w == 0:
                dp[no_of_val][w] = 0
            elif values[no_of_val - 1] <= w:
                dp[no_of_val][w] = max(
                    values[no_of_val - 1] + dp[no_of_val - 1][w - weights[no_of_val - 1]],
                    dp[no_of_val - 1][w],
                )
            else:
                dp[no_of_val][w] = dp[no_of_val - 1][w]

    return dp[no_of_vals][condition_weight]


if __name__ == "__main__":
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
    print(knapsack(W, wt, val, n))
