"""
    Created by Mustafa Sencer Özcan on 20.05.2020.

    Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
    Find all unique triplets in the array which gives the sum of zero.
"""
from typing import List, Set, Tuple


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

    def three_sum_2(self, nums: List[int]) -> Set:
        result = set()
        nums.sort()
        for i in range(1, len(nums) - 1):
            left, right = i - 1, i + 1

            while len(nums) > right > left >= 0:
                triplet_sum = nums[left] + nums[i] + nums[right]

                if triplet_sum > 0:
                    left -= 1
                    continue
                elif triplet_sum < 0:
                    right += 1
                    continue
                else:
                    result.add((nums[left], nums[i], nums[right]))
                    right += 1
                    left -= 1

        return result


if __name__ == '__main__':
    input = [-1, -1, 1, 2, -1, -4, 2, -2, -3, 6]
    result = Solution().solve(input)
    result_1 = Solution().three_sum(input)
    assert result == result_1
