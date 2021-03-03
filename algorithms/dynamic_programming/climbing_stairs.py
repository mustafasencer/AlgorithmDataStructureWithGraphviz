"""
    Created by Mustafa Sencer Özcan on 22.05.2020.

    You are climbing a stair case. It takes n steps to reach to the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    Note: Given n will be a positive integer.
"""


class Solution:
    def climb_stairs(self, n: int) -> int:
        if n == 0:
            return 0
        a = 0
        b = 1
        for _ in range(n):
            c = a + b
            a = b
            b = c
        return b

    def solution_1(self, n):
        if n == 0:
            return 0

        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]


if __name__ == '__main__':
    result = Solution().solution_1(5)
    result__ = Solution().climb_stairs(5)
    assert result == result__
    print(result)
