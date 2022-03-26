"""
Absolute distinct count
Array is sorted!
Hint: Leveraging sorted array would enable the solution to use only O(1) extra space.
"""
from typing import List


def solve(nums: List[int]) -> int:
    distinct = set()
    for value in nums:
        distinct.add(abs(value))

    return len(distinct)


def solve_2(nums: List[int]) -> int:
    count = len(nums)

    i, j = 0, len(nums) - 1

    while i < j:

        # Clear negative duplicates from the array
        while nums[i] == nums[i + 1]:
            count -= 1
            i += 1

        # Clear positive duplicates from the array
        while nums[j] == nums[j - 1]:
            count -= 1
            j -= 1

        if j == i:
            break

        sum = nums[i] + nums[j]

        if sum == 0:
            i += 1
            j -= 1
            count -= 1

        if sum > 0:
            j -= 1
        elif sum < 0:
            i += 1

    return count


if __name__ == '__main__':
    nums = [-5, -3, 0, 1, 3, 3]
    result = solve_2(nums)
    assert result == 4
