"""
Longest increasing sub sequence
https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/
"""


def solution(array):
    dp = [1] * len(array)

    for i in range(1, len(array)):
        for j in range(i):
            if array[j] < array[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    return max(dp)


def solution_2(array):
    dp = [1] * len(array)

    for i in range(1, len(array)):
        for j in range(i):
            if array[i] > array[j]:
                dp[i] = max(dp[:j + 1]) + 1

    return max(dp)


if __name__ == '__main__':
    array = [0, 1, 0, 3, 2, 3]
    result = solution(array)
    assert result == 4
