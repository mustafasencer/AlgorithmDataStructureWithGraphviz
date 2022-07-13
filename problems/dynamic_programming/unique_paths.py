"""
    A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

    The robot can only move either down or right at any point in time.
    The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

    How many possible unique paths are there?
"""


def solutions(m: int, n: int) -> int:
    dp = [[1 for _ in range(m)] for _ in range(n)]
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    return dp[n - 1][m - 1]


if __name__ == "__main__":
    result = solutions(27, 10)
    assert result == []
