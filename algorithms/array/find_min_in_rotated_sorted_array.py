"""
    Created by Mustafa Sencer Özcan on 27.05.2020.
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
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
    result = Solution().findMin([3, 4, 5, 0, 1, 2])
    print(result)
