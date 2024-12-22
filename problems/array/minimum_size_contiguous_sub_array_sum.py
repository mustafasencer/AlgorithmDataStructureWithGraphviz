def solution(nums, target):
    """
    1. keep the window sum of the elements
    2. remove the first item in the window to keep exploring the next contiguous sub arrays
    """
    INF = len(nums) + 1
    min_length = INF
    window_sum = 0
    left = 0

    for i in range(len(nums)):
        window_sum += nums[i]
        while window_sum >= target:
            min_length = min(min_length, i - left + 1)
            window_sum -= nums[left]
            left += 1

    return min_length if min_length != INF else 0


if __name__ == "__main__":
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    result = solution(nums, target)
    assert result == 2
