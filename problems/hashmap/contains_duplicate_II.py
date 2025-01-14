"""
1. Check if nums array contains duplicates within an index distance <= k.
"""


def solution(nums: list[int], k: int) -> bool:
    lookup = {}
    for i in range(len(nums)):
        if nums[i] in lookup and abs(i - lookup[nums[i]]) <= k:
            return True
        lookup[nums[i]] = i

    return False


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    k = 3
    result = solution(nums, k)
    assert result is True
