"""
    Created by Mustafa Sencer Özcan on 19.05.2020.

    Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

    Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.
"""
from typing import List


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        index = 0
        for value in nums:
            if index < 2 or nums[index - 2] < value:
                nums[index] = value
                index += 1
        return len(nums[:index])

    def solution_1(self, nums: List[int]) -> int:

        i = 1
        count = 2
        while i < len(nums):

            if nums[i] - nums[i - 1] == 0 and count < 2:
                nums[:] = nums[:i] + nums[i + 1:]
                count += 1
            elif nums[i] - nums[i - 1] == 0:
                i += 1
                count += -1
            else:
                i += 1
                count = 2

        return len(nums)


if __name__ == '__main__':
    result = Solution().solution_1([1, 1, 1, 2, 2, 3])
    assert result == 5
    print(result)
