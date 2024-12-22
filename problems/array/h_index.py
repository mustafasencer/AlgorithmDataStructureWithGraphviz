from typing import List


def solve(nums: List[int]):
    """
    1. loop over the reversed nums
    2. check if the value is less than the index + 1
    3. index will give the h index, thus break the loop
    """
    nums.sort(reverse=True)
    h_index = 0
    for i in range(len(nums)):
        if nums[i] < i + 1:
            h_index = i
            break

    return h_index


if __name__ == "__main__":
    nums = [3, 0, 6, 1, 5]
    result = solve(nums)
    assert result == 3
