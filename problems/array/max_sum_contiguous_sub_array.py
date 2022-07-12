"""
    Given an integer array nums, find the contiguous subarray (containing at least one number)
    which has the largest sum and return its sum.
"""
from typing import List


def solution(nums: List[int]) -> int:
    """ """
    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
    return max(nums)


def solution_1(nums):
    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]

    return nums[-1]


def solution_2(nums):
    first_value = nums[0]
    dp = [first_value] * len(nums)
    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            dp[i] = nums[i] + dp[i - 1]
        else:
            dp[i] = nums[i]

    return max(dp)


if __name__ == "__main__":
    array = [1, 3, -5, 5, 2, 3]
    result = solution(array)
    assert result == 10
