"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
"""


def solution(prices: list[int]) -> int:
    if not prices:
        return 0

    dp = [0] * len(prices)
    min_ = prices[0]

    for i in range(1, len(prices)):
        profit = prices[i] - min_

        if profit > 0:
            dp[i] = profit
        else:
            dp[i] = 0

        min_ = min(min_, prices[i])

    return max(dp)


def solution_v2(prices):
    """
    1. start looping from the 1st index
    2. substract the previous index (memoized)
    3. store the max value in a separate variable
    4. in each loop get the max of the substraction result and in-place update the variable
    5. update the memoized store with the min value (by comparing with the currently looped value)
    -> 1, 2, 3, 4, 5
          ^
    """
    dp = [0] * len(prices)
    dp[0] = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        current = prices[i] - dp[i - 1]

        max_profit = max(current, max_profit)

        dp[i] = min(dp[i - 1], prices[i])

    return max_profit


def brute_force(prices):
    max_profit = 0
    for i in range(1, len(prices)):
        for j in range(i):
            max_profit = max(prices[i] - prices[j])

    return max_profit


if __name__ == "__main__":
    result = brute_force([7, 1, 5, 3, 6, 4])
    assert result == 5
