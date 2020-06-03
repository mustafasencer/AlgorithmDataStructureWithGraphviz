"""
    Created by Mustafa Sencer Özcan on 21.05.2020.

    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

    (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

    You are given a target value to search. If found in the array return its index, otherwise return -1.

    You may assume no duplicate exists in the array.

    Your algorithm's runtime complexity must be in the order of O(log n).
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
                return target
            if nums[real_mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1


if __name__ == '__main__':
    result = Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
    print(result)
