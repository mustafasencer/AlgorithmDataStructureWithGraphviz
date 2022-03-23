"""
    Created by Mustafa Sencer Özcan on 21.05.2020.

    Given an array of non-negative integers, you are initially positioned at the first index of the array.

    Each element in the array represents your maximum jump length at that position.

    Determine if you are able to reach the last index.
"""
from typing import List


class Solution:
    def can_jump(self, nums: List[int]) -> bool:
        n = len(nums)
        last = n - 1
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= last:
                last = i
        return last <= 0


if __name__ == '__main__':
    result = Solution().can_jump([2, 2, 1, 1, 4])
    print(result)
