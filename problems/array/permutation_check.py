"""
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].
"""


def solution(nums):
    """
    1. sort the nums array and check if a value is missing from the sequence
    """
    nums.sort()
    prev = nums[0]
    for item in nums[1:]:
        subs = item - prev
        if subs != 1:
            return 0
        prev = item
    return 1


def solution_1(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if not nums[i] - nums[i - 1] == 1:
            return 0
    return 1


if __name__ == "__main__":
    nums = [1, 3, 4]
    result = solution_1(nums)
    assert result == 0
