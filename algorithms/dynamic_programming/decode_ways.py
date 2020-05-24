"""
    Created by Mustafa Sencer Özcan on 23.05.2020.
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        dp = [1, 1 if s[0] != '0' else 0]
        for i in range(2, n + 1):
            first = int(s[i - 1: i])
            second = int(s[i - 2: i])
            if 0 < first <= 9:
                dp.append(dp[i - 1])
            if 10 <= second <= 26:
                dp[i] += dp[i - 2]
        return dp[n]


if __name__ == '__main__':
    result = Solution().numDecodings("10")
    print(result)
