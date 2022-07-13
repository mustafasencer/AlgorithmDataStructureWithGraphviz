"""
Longest increasing sub sequence
https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/
https://leetcode.com/problems/longest-increasing-subsequence/
"""


def solution(nums):
    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    return max(dp)


def solution_2(nums):
    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[: j + 1]) + 1

    return max(dp)


if __name__ == "__main__":
    nums = [1, 101, 2, 3, 100, 4, 5]
    result = solution(nums)
    assert result == 5
