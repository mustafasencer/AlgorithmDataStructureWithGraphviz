"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.
"""


def solution(s: str):
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
