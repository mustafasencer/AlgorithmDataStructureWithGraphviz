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


def solve_2(nums: List[int]) -> int:
    """
    1. loop over the nums array starting from the 1st index
    2. for every index go back and check if the addition of i and j th item are >= than i
    3. if so just add it to the dp array with + 1
    4. last item in dp is the min amount of moves necessary to reach end of array
    """
    dp = [0] * len(nums)

    for i in range(1, len(nums)):
        j = 0
        while j < i:
            if j + nums[j] >= i:
                dp[i] = dp[j] + 1
                break
            j += 1
        print(f"dp: {dp}")

    return dp[-1]


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    result = solve(nums)
    assert result == 2
