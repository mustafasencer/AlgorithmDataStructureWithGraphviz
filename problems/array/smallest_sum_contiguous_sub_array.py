import sys


def solution(nums: list[int]) -> int:
    """
    1. loop over the nums array and check if `current_min` is bigger than 0
    2. > 0 means that the item does not contribute to the smallest value (single positive is already smaller!)
     then refresh the value
    3. < 0 means the value is negative and consequently should be added to get an even smaller number.
    """
    current_min = sys.maxsize

    ultimate_min = sys.maxsize

    for i in range(len(nums)):
        if current_min > 0:
            current_min = nums[i]
        else:
            current_min += nums[i]

        ultimate_min = min(current_min, ultimate_min)

    return ultimate_min


if __name__ == "__main__":
    nums = [3, -4, 2, -3, -1, 7, -5]
    result = solution(nums)
    assert result == -6
