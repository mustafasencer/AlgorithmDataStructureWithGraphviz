"""
    Created by Mustafa Sencer Özcan on 24.05.2020.
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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


if __name__ == '__main__':
    result = Solution().maxProfit([7, 1, 5, 3, 6, 4])
    print(result)
