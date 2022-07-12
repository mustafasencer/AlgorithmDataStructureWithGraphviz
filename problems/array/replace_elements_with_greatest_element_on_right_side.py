"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right,
 and replace the last element with -1.

After doing so, return the array.
"""
from typing import List


def solution(nums: List[int]):
    """
    1. no explanation!
    """
    result = []

    for i in range(len(nums)):
        nums.pop(0)
        if not nums:
            result.append(-1)
        else:
            result.append(max(nums))
    return result


def solution_2(nums: List[int]):
    mx = -1
    for i in range(len(nums) - 1, -1, -1):
        nums[i], mx = mx, max(mx, nums[i])
    return nums


def solution_3(nums: List[int]):
    """
    1. O(1) extra space
    2. best solution in my opinion!
    """
    for i in range(len(nums)):
        if i == len(nums) - 1:
            value = -1
        else:
            value = max(nums[i + 1 :])
        nums[i] = value

    return nums


if __name__ == "__main__":
    nums = [21, 18, 5, 4, 6, 1]
    result = solution(nums)
    assert result == [18, 6, 6, 6, 1, -1]
