"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
"""


def solution(nums: list[int], target: int) -> int:
    """
    1. binary search the smallest element in the nums array
    2. this will give the rotation shift
    3. the rotation value should be used to find the target
        (now we can think of the shifted mid values as sorted array indices)
    4. return -1 if target not found.
    """
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = int((high + low) / 2)
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid

    rot = low
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = int((high + low) / 2)
        real_mid = (mid + rot) % len(nums)
        if nums[real_mid] == target:
            return real_mid
        if nums[real_mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    result = solution([4, 5, 6, 7, 0, 1, 2], 0)
    assert result == 4
