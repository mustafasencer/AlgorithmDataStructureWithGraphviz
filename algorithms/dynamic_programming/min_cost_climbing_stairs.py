"""
    Created by Mustafa Sencer Özcan on 22.05.2020.
"""
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min1, min2 = cost[0], cost[1]
        for c in cost[2:]:
            min1, min2 = min2, min(min1, min2) + c
        return min(min1, min2)


if __name__ == '__main__':
    result = Solution().minCostClimbingStairs([10, 15, 20])
    print(result)
