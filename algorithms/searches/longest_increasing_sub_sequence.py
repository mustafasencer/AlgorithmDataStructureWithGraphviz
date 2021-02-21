"""
Max sum increasing sub sequence
"""


def max_sum_is(nums):
    tails = [0] * len(nums)
    size = 0
    for x in nums:
        i, j = 0, size
        while i != j:
            m = int((i + j) / 2)
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
    return size


if __name__ == '__main__':
    arr = [1, 101, 2, 3, 100, 4, 5]
    length = len(arr)
    print(f"Sum of maximum sum increasing subsequence is {max_sum_is(arr)}")
