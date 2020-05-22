from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)


if __name__ == '__main__':
    array = [1, 3, -5, 5, 2, 3]
    result = Solution().maxSubArray(array)
