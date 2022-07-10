"""
https://leetcode.com/problems/jump-game-ii/
"""
from typing import List


def solve(nums: List[int]) -> int:
    if len(nums) < 2:
        return 1

    times = 1
    left, right = 0, nums[0]
    while right < len(nums) - 1:
        times += 1
        nxt = max(i + nums[i] for i in range(left, right + 1))
        left, right = right, nxt

    return times


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    result = solve(nums)
    assert result == 2
