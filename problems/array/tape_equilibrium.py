"""
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts:
    A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of:
    |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7
Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].
"""


def solution(nums: list[int]) -> int:
    all_sum = sum(nums)
    sum_first = 0

    min_value = float("inf")

    for i in range(1, len(nums)):
        sum_first += nums[i]
        sum_second = all_sum - sum_first

        difference = abs(sum_first - sum_second)
        min_value = min(min_value, difference)

    return min_value


def solution_2(nums: list[int]) -> int:
    """
    🥉
    1. loop over the nums array
    2. find the diff for each required index.
    """
    min_value = abs(sum(nums[:1]) - sum(nums[1:]))
    for i in range(2, len(nums)):
        min_value = min(abs(sum(nums[:i]) - sum(nums[i:])), min_value)
    return min_value


if __name__ == "__main__":
    nums = [3, 1, 2, 4, 3]
    result = solution_2(nums)
    assert result == 1
