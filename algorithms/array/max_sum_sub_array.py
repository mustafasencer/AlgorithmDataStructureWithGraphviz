"""
    Created by Mustafa Sencer Özcan on 26.05.2020.

    Given an integer array nums, find the contiguous subarray (containing at least one number)
    which has the largest sum and return its sum.
"""
from typing import List


class Solution:
    def max_cont_sub_array(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)


if __name__ == '__main__':
    array = [1, 3, -5, 5, 2, 3]
    result = Solution().max_cont_sub_array(array)
    print(result)
