"""
Given an integer array nums, you need to find one continuous subarray that
if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.
"""


def solution(nums: list[int]) -> int:
    """1."""
    if len(nums) < 2:
        return 0

    end = 0
    prev = nums[0]

    for i in range(len(nums)):
        if prev > nums[i]:
            end = i
        else:
            prev = nums[i]

    start = 0
    prev = nums[len(nums) - 1]
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] > prev:
            start = i
        else:
            prev = nums[i]

    if not end:
        return 0

    return end - start + 1


def solution_1(nums):
    prev = nums[0]
    end = 0

    for i in range(len(nums)):
        if nums[i] < prev:
            end = i
        else:
            prev = nums[i]

    start = 0
    prev = nums[len(nums) - 1]

    for i in range(len(nums) - 1, -1, -1):
        if prev < nums[i]:
            start = i
        else:
            prev = nums[i]

    if end == 0:
        return 0

    return end - start + 1


def solution_2(nums):
    start = 0

    for i in range(1, len(nums)):
        prev = i - 1
        if nums[i] < nums[prev]:
            start = prev
            break

    end = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        prev = i - 1
        if nums[i] < nums[prev]:
            end = i
            break

    return end - start + 1


if __name__ == "__main__":
    nums = [2, 6, 4, 8, 10, 9, 15]
    result = solution_1(nums)
    assert result == 5
