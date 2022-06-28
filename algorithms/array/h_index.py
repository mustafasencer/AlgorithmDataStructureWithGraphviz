from typing import List


def solve(nums: List[int]):
    nums.sort(reverse=True)
    h_index = 0
    for i in range(len(nums)):
        if nums[i] <= i + 1:
            h_index = nums[i]
            break

    return h_index


if __name__ == '__main__':
    nums = [3, 0, 6, 1, 5]
    result = solve(nums)
    assert result == 3
