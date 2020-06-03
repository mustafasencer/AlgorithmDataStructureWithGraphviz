"""
    Created by Mustafa Sencer Özcan on 22.05.2020.

    On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

    Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor,
    and you can either start from the step with index 0, or the step with index 1.
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
