"""
    A message containing letters from A-Z is being encoded to numbers using the following mapping:

    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26
    Given a non-empty string containing only digits, determine the total number of ways to decode it.
"""


def solution(s: str) -> int:
    if not s:
        return 0

    n = len(s)
    dp = [1 if s[0] != "0" else 0]

    for i in range(2, n + 1):
        first = int(s[i - 1 : i])
        second = int(s[i - 2 : i])
        if 0 < first <= 9:
            dp.append(dp[i - 1])
        if 10 <= second <= 26:
            dp[i] += dp[i - 2]

    return dp[n]


def solution_1(s: str):
    """
    1. create a dp array
    2. based on the digits and number with 2 basamaks increase the possibility count in the dp array
    """
    if not s:
        return 0

    dp = [0] * len(s)
    dp[0] = 1 if s[0] != "0" else 0

    for i in range(1, len(s)):
        dp[i] = dp[i - 1]

        if 10 <= int(s[i - 1 : i + 1]) <= 26:
            dp[i] += 1

        if s[i] != "0":
            dp[i] += 1

    return dp[-1]


if __name__ == "__main__":
    result = solution("1010011")
    assert result == 7
