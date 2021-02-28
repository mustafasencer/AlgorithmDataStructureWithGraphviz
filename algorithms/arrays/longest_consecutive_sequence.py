"""
    Created by Mustafa Sencer Özcan on 25.05.2020.

    Given an unsorted arrays of integers, find the length of the longest consecutive elements sequence.

    Your algorithm should run in O(n) complexity.
"""
from typing import List


class Solution:
    # O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for i in nums:
            if i - 1 not in nums:
                j = i + 1
                while j in nums:
                    j += 1
                res = max(j - i, res)
        return res

    # O(nlog(n)) dp approach
    def dp_approach(self, nums):
        if not nums:
            return 0
        nums.sort()
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                dp[i] = dp[i - 1] + 1
            elif nums[i] - nums[i - 1] == 0:
                dp[i] = dp[i - 1]
            else:
                dp[i] = 1
        return max(dp)


if __name__ == '__main__':
    result = Solution().longestConsecutive([1, 2, 0, 1, 4, 5, 6, 7])
    assert result == 4
    print(result)
