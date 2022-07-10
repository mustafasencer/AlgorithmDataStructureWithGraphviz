"""
    Created by Mustafa Sencer Özcan on 19.05.2020.
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = {}
        for i, value in enumerate(nums):
            n = target - value
            if n in dict_:
                return [dict_[n], i]
            else:
                dict_[value] = i

    def two_sum(self, nums, target):
        lookup = {}
        for i in range(len(nums)):
            remaining = target - nums[i]

            if remaining in lookup:
                return [lookup[remaining], i]
            else:
                lookup[nums[i]] = i
        return


if __name__ == "__main__":
    result = Solution().twoSum([2, 7, 11, 15], 9)
    result_2 = Solution().two_sum([2, 7, 11, 15], 9)
    assert result == result_2
