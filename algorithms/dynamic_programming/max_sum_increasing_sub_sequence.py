"""
Longest increasing sub sequence
https://www.geeksforgeeks.org/maximum-sum-increasing-subsequence-dp-14/
"""


def solution(input):
    dp = [0] * len(input)

    for i in range(len(input)):
        dp[i] = input[i]

    for i in range(1, len(input)):
        for j in range(i):
            if input[j] < input[i] and dp[i] < (dp[i] + input[j]):
                dp[i] = dp[i] + input[j]
    return max(dp)


if __name__ == '__main__':
    input = [1, 101, 2, 3, 100, 4, 5]
    result = solution(input)
    assert result == 106
    print(result)
