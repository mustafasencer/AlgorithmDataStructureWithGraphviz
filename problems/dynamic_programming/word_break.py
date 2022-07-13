from typing import List


def solution(s: str, word_dict: List[str]) -> bool:
    dp = [False] * len(s)
    for i in range(len(s)):
        for w in word_dict:
            if s[i - len(w) + 1: i + 1] == w and (
                    dp[i - len(w)] or i - len(w) == -1
            ):
                dp[i] = True
    return dp[-1]


def solution_1(s, word_dict):
    dp = [False]

    for i in range(len(s)):
        for word in word_dict:
            if s[i - len(word) + 1: i + 1] == word and (dp[1]):
                pass

    return dp[-1]


if __name__ == "__main__":
    result = solution("leetcode", ["leet", "code"])
    result_2 = solution_1("aaaaaaa", ["aaaa", "aaa"])
    assert result == result_2
