"""
    Created by Mustafa Sencer Özcan on 21.05.2020.
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        last = n - 1
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= last:
                last = i
        return last <= 0


if __name__ == '__main__':
    result = Solution().canJump([2, 2, 1, 0, 4])
    print(result)
