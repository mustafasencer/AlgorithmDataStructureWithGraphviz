"""
    Created by Mustafa Sencer Özcan on 23.05.2020.
    
    A message containing letters from A-Z is being encoded to numbers using the following mapping:

    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26
    Given a non-empty string containing only digits, determine the total number of ways to decode it.
"""


class Solution:
    def num_decodings(self, s: str) -> int:
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

    def _test(self, s):
        if not s:
            return 0

        dp = [1 if s[0] != "0" else 0]
        dp[1] = dp[0] + 1 if s[1] != "0" else 0

        for index in range(2, len(s)):
            first = dp[index - 1]
            second = dp[index - 2: index]

            if 0 < int(first) <= 9:
                dp[index] = dp[index - 1] + 1
            if 10 <= int(second) <= 26:
                dp[index] = dp[index - 1] + 1

        return dp[-1]


if __name__ == '__main__':
    result = Solution().num_decodings("111")
    print(result)
