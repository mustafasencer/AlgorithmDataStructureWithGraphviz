from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        shortest = []
        max_value = nums[0]
        for i in range(len(nums)):
            if max_value > nums[i]:
                shortest.append()
            else:
                max_value = nums[i]

if __name__ == '__main__':
    nums = [2, 6, 4, 8, 10, 9, 15]
    nums = [6, 2, 3, 4, 5]
    result = Solution().findUnsortedSubarray(nums)
    assert result == 5
    print(result)
