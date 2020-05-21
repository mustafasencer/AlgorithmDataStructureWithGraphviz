"""
    Created by Mustafa Sencer Özcan on 21.05.2020.
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
