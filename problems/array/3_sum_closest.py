"""
https://leetcode.com/problems/3sum-closest/
find the closest sum of 3 items that are closest to target
"""

from typing import List


def solve(nums: List[int], target: int):
    """
    1. sort the nums array
    2. loop over the nums array with 2 pointers situated; one next to i and one at the end of nums array
    3. increase and decrease the pointers to cover the entire nums array
    """
    nums.sort()
    closest_3_sum = nums[0] + nums[1] + nums[2]

    for i in range(len(nums) - 2):
        j, k = i + 1, len(nums) - 1

        while j < k:
            current_sum = nums[i] + nums[j] + nums[k]

            if current_sum > target:
                k -= 1

            if current_sum < target:
                j += 1

            if abs(target - current_sum) < abs(target - closest_3_sum):
                closest_3_sum = current_sum

    return closest_3_sum


if __name__ == "__main__":
    nums = [1, 2, -1, 4]
    target = 1
    result = solve(nums, target)
    assert result == 2
