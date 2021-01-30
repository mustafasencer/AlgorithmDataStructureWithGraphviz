from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        end = 0
        prev = nums[0]

        for i in range(len(nums)):
            if prev > nums[i]:
                end = i
            else:
                prev = nums[i]

        start = 0
        prev = nums[len(nums) - 1]
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > prev:
                start = i
            else:
                prev = nums[i]

        if not end:
            return 0

        return end - start + 1


if __name__ == '__main__':
    # nums = [2, 6, 4, 8, 10, 9, 15]
    nums = [5, 4, 3, 2, 1]
    result = Solution().findUnsortedSubarray(nums)
    assert result == 2
    print(result)
