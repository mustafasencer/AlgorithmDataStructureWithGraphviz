"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""


def solution(n: int) -> int:
    """
    1. first step has 1 different ways to reach
    2. second step has 2 different ways to reach
    3. third step has 3 different steps to reach
    4. modeling the problem as a DP solves it directly.
    """
    if n == 0:
        return 0
    a = 0
    b = 1
    for _ in range(n):
        c = a + b
        a = b
        b = c
    return b


def solution_v2(n):
    if n == 0:
        return 0

    dp = [0] * n
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[-1]


if __name__ == "__main__":
    result = solution_v2(5)
    result__ = solution(5)
    assert result == result__
