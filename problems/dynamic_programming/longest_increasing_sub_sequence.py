"""
Longest increasing sub sequence
https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/
https://leetcode.com/problems/longest-increasing-subsequence/
"""
from typing import List


def solution(nums: List[int]):
    """
    1. loop over the nums array
    2. nested loop until the i the index in order to check from the beginning the length of the increasing sequence
    3. return dp max
    """
    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    return max(dp)


if __name__ == "__main__":
    nums = [1, 2, 101, 1, 4, 100, 5, 6]
    result = solution(nums)
    assert result == 5
