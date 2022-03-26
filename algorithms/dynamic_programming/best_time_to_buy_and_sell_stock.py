"""
    Created by Mustafa Sencer Özcan on 24.05.2020.

    Say you have an array for which the ith element is the price of a given stock on day i.

    If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
    design an algorithm to find the maximum profit.

    Note that you cannot sell a stock before you buy one.
"""
from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:

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

    def solution_1(self, prices):
        dp = [prices[0]] * len(prices)
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < dp[i]:
                dp[i] = prices[i]
            max_profit = max(prices[i] - min(dp[:i]), max_profit)
        return max_profit

    def solution_2(self, prices):
        dp = [0] * len(prices)

        for i in range(1, len(prices)):
            dp[i] = prices[i] - min(prices[:i])
        return max(dp)


if __name__ == '__main__':
    result = Solution().max_profit([7, 1, 5, 3, 6, 4])
    assert result == 5
    print(result)
