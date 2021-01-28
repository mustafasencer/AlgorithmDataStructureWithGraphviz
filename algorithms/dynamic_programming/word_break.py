"""
    Created by Mustafa Sencer Özcan on 25.05.2020.
"""
from typing import List


class Solution:
    def word_break(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                if s[i - len(w) + 1: i + 1] == w and (dp[i - len(w)] or i - len(w) == -1):
                    dp[i] = True
        return dp[-1]


if __name__ == '__main__':
    result = Solution().word_break("leetcode", ["leet", "code"])
    print(result)
