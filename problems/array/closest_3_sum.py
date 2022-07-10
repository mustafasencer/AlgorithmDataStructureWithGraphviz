"""
https://leetcode.com/problems/3sum-closest/
"""

from typing import List


def solve(nums: List[int], target: int):
    nums.sort()
    sum_value = nums[0] + nums[1] + nums[2]

    for i in range(len(nums) - 2):

        j, k = i + 1, len(nums) - 1

        while j < k:

            current_sum = nums[i] + nums[j] + nums[k]

            if current_sum > target:
                k -= 1

            if current_sum < target:
                j += 1

            if abs(target - current_sum) < abs(target - sum_value):
                sum_value = current_sum

    return sum_value


if __name__ == "__main__":
    nums = [1, 2, -1, 4]
    target = 1
    result = solve(nums, target)
    assert result == 2
