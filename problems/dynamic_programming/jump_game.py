"""
    Given an array of non-negative integers, you are initially positioned at the first index of the array.

    Each element in the array represents your maximum jump length at that position.

    Determine if you are able to reach the last index.
"""
from typing import List


def solution(nums: List[int]) -> bool:
    """
    1. start looping over the nums array in reverse order
    2. just add the current index to the nums[index] and check if it is >= target
    3. if it is the case return True
    """
    n = len(nums)
    last = n - 1
    for i in range(n - 2, -1, -1):
        if i + nums[i] >= last:
            last = i
    return last <= 0


if __name__ == "__main__":
    result = solution([2, 2, 1, 1, 4])
    assert result is True
