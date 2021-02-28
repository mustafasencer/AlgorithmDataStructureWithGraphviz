"""
    Created by Mustafa Sencer Özcan on 27.05.2020.

    Suppose an arrays sorted in ascending order is rotated at some pivot unknown to you beforehand.

    (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

    Find the minimum element.

    You may assume no duplicate exists in the arrays.
"""
from typing import List


class Solution:
    def find_min(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = int((high + low) / 2)
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return nums[low]

    def test_(self, nums: List[int]):
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = int((high + low) / 2)
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return nums[low]


if __name__ == '__main__':
    result = Solution().find_min([3, 4, 5, 0, 1, 2])
    print(result)
