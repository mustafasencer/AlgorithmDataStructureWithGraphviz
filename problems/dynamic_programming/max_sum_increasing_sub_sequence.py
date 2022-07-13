"""
Longest increasing sub sequence
https://www.geeksforgeeks.org/maximum-sum-increasing-subsequence-dp-14/
"""


def solution(nums):
    dp = [0] * len(nums)

    for i in range(len(nums)):
        dp[i] = nums[i]

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i] and dp[i] < (dp[i] + nums[j]):
                dp[i] = dp[i] + nums[j]
    return max(dp)


if __name__ == "__main__":
    nums = [1, 101, 2, 3, 100, 4, 5]
    result = solution(nums)
    assert result == 106
