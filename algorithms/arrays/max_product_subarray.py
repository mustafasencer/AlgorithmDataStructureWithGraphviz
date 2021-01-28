"""
    Created by Mustafa Sencer Özcan on 26.05.2020.

    Given an integer arrays nums, find the contiguous subarray
    within an arrays (containing at least one number) which has the largest product.
"""
from typing import List
from functools import reduce


class Solution:
    def max_product(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            k = i + 1
            while k < len(nums):
                result = max(reduce(lambda x, y: x * y, nums[i: k + 1]), result, 0)
                k += 1
        return result

    def _test(self, nums):
        nums_copy = nums[::-1]
        for i in range(len(nums)):
            nums[i] *= nums[i - 1] or 1
            nums_copy[i] *= nums[i - 1] or 1
        return max(nums + nums_copy)


if __name__ == '__main__':
    result = Solution().max_product([-2, 2, 3])
    result_ = Solution()._test([-2, 2, 3])
    assert result == result_
    print(result)
