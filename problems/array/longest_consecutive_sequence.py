"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.
"""

from typing import List


# O(n)
def longest_consecutive(nums: List[int]) -> int:
    """
    1. construct a set
    2. loop over the set and check if the number has a preceding number in it
    3. if doesn't then it means we have a start of consecutive sequence
    4. continue looping over it unless you have a next in the sequence
    """
    nums = set(nums)
    res = 0
    for i in nums:
        if i - 1 not in nums:
            j = i + 1
            while j in nums:
                j += 1
            res = max(j - i, res)
    return res


# O(nlog(n)) dp approach
def dp_approach(nums: List[int]) -> int:
    """
    1. sort the given nums array
    2. construct a dp array where first item is given the value of 1 because it is the starter of a potential sequence
    3. increase dp value if the difference between current and next item is 1!
    4. if values equal keep the same value as the preceding value
    5. else reset the dp value
    """
    if not nums:
        return 0
    nums.sort()
    dp = [0] * len(nums)
    dp[0] = 1
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] == 1:
            dp[i] = dp[i - 1] + 1
        elif nums[i] - nums[i - 1] == 0:
            dp[i] = dp[i - 1]
        else:
            dp[i] = 1
    return max(dp)


if __name__ == "__main__":
    result = longest_consecutive([1, 2, 0, 1, 4, 5, 6, 7])
    assert result == 4
