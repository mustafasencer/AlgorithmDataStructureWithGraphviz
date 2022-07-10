"""
    Created by Mustafa Sencer Özcan on 25.05.2020.
"""
from typing import List


class Solution:
    def word_break(self, s: str, word_dict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for w in word_dict:
                if s[i - len(w) + 1 : i + 1] == w and (
                    dp[i - len(w)] or i - len(w) == -1
                ):
                    dp[i] = True
        return dp[-1]

    def word_break_2(self, s, word_dict):
        dp = [False]

        for i in range(len(s)):
            for word in word_dict:
                if s[i - len(word) + 1 : i + 1] == word and (dp[1]):
                    pass

        return dp[-1]


if __name__ == "__main__":
    result = Solution().word_break("leetcode", ["leet", "code"])
    result_2 = Solution().word_break_2("aaaaaaa", ["aaaa", "aaa"])
    print(result)
