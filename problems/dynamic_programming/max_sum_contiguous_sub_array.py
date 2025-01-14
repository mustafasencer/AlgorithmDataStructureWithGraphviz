"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
"""


def solution(nums: list[int]) -> int:
    """
    1. loop over the nums array beginning from index 1
    2. if previous item in the array is > 0 then add it and set the value to the current index
    3. return max of the nums array.
    """
    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
    return max(nums)


def solution_1(nums):
    """
    1. same approach as above 👆
    2. the only difference is that extra O(N) space complexity is added.
    """
    first_value = nums[0]
    dp = [first_value] * len(nums)
    for i in range(1, len(nums)):
        if dp[i - 1] > 0:
            dp[i] = nums[i] + dp[i - 1]
        else:
            dp[i] = nums[i]

    return max(dp)


if __name__ == "__main__":
    array = [1, 3, -3, 5, 2, 3]
    result = temp(array)
    assert result == 11
