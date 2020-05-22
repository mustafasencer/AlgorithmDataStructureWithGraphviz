"""
    Created by Mustafa Sencer Özcan on 22.05.2020.
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for i in range(m)] for j in range(n)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[n - 1][m - 1]


if __name__ == '__main__':
    result = Solution().uniquePaths(27, 10)
    print(result)
