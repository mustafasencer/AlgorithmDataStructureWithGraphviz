"""
    Created by Mustafa Sencer Özcan on 27.05.2020.
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0] * len(nums)
        for i in range(len(nums)):
            if i < 2:
                dp[i] = nums[i]
            else:
                dp[i] = nums[i] + max(dp[:i - 1])
        return max(dp)


if __name__ == '__main__':
    result = Solution().rob([2, 1, 1, 2, 7])
    print(result)
