"""
    Created by Mustafa Sencer Özcan on 20.05.2020.

    Given an arrays nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
    Find all unique triplets in the arrays which gives the sum of zero.
"""
from typing import List


class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        length = len(nums)

        for i in range(length - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, length - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1

        return result


if __name__ == '__main__':
    result = Solution().three_sum([-1, -1, 1, 2, -1, -4])
    print(result)
