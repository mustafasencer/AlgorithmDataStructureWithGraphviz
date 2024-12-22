"""
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
nums non-empty array nums of M integers is given. This array represents consecutive operations:

if nums[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if nums[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array nums such that:

    nums[0] = 3
    nums[1] = 4
    nums[2] = 4
    nums[3] = 6
    nums[4] = 1
    nums[5] = 4
    nums[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

def solution(N, nums)

that, given an integer N and a non-empty array nums consisting of M integers, returns a sequence of integers representing
the values of the counters.

Result array should be returned as an array of integers.

For example, given:

    nums[0] = 3
    nums[1] = 4
    nums[2] = 4
    nums[3] = 6
    nums[4] = 1
    nums[5] = 4
    nums[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..100,000];
each element of array nums is an integer within the range [1..N + 1].
"""


def solution(N, nums):
    """
    1.
    """
    counters = [0] * N
    max_counter = 0

    for i in range(len(nums)):
        value = nums[i]
        if value == N + 1:
            counters = [max_counter] * N
        else:
            counters[value - 1] += 1
            max_counter = max(max_counter, counters[value - 1])

    return counters


if __name__ == "__main__":
    N = 5
    nums = [3, 4, 4, 6, 1, 4, 4]
    result = solution(N, nums)
    assert result == [3, 2, 2, 4, 2]
