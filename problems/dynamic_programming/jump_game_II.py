"""https://leetcode.com/problems/jump-game-ii/."""


def solution(nums: list[int]) -> int:
    if len(nums) < 2:
        return 1

    times = 1
    left, right = 0, nums[0]
    while right < len(nums) - 1:
        times += 1
        nxt = max(i + nums[i] for i in range(left, right + 1))
        left, right = right, nxt

    return times


def solution_v2(nums: list[int]) -> int:
    """
    1. loop over the nums array starting from the 1st index
    2. for every index go back and check if the addition of i and j th item are >= than i
    3. if so just add it to the dp array with + 1
    4. last item in dp is the min amount of moves necessary to reach end of array.
    """
    dp = [0] * len(nums)

    for i in range(1, len(nums)):
        j = 0
        while j < i:
            if j + nums[j] >= i:
                dp[i] = dp[j] + 1
                break
            j += 1

    return dp[-1]


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4, 1, 1, 1, 0]
    result = solution_v2(nums)
    assert result == 3
