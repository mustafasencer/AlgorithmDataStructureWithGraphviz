import sys
from typing import List


def solution(nums: List[int]) -> int:
    """
    1. loop over the nums array and check if `min_ending_here` is bigger than 0
    2. > 0 means that the item does not contribute to the smallest value (single positive is already smaller!)
     then refresh the value
    3. < 0 means the value is negative and consequently should be added to get an even smaller number
    """
    min_ending_here = sys.maxsize

    min_so_far = sys.maxsize

    for i in range(len(nums)):

        if min_ending_here > 0:
            min_ending_here = nums[i]
        else:
            min_ending_here += nums[i]

        min_so_far = min(min_ending_here, min_so_far)

    return min_so_far


if __name__ == "__main__":
    nums = [3, -4, 2, -3, -1, 7, -5]
    result = solution(nums)
    assert result == -6
