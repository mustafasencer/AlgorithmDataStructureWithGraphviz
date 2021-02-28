"""
Longest increasing sub sequence
https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/
"""


def solution(nums):
    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    return max(dp)


if __name__ == '__main__':
    arr = [1, 101, 2, 3, 100, 4, 5, 7, 10]
    result = solution(arr)
    assert result == 7
