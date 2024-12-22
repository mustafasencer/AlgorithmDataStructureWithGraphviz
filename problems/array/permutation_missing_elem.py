"""
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)],
 which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

class Solution { public int solution(int[] A); }

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
"""


def solution(nums):
    """
    https://leetcode.com/problems/missing-number/
    1. check if the sequence overall sum has a missing element.
    """
    n = len(nums)
    sum_ = n * (n + 1) // 2
    return sum_ - sum(nums)


if __name__ == "__main__":
    nums = [2, 3, 1, 5]
    result = solution(nums)
    assert result == 4
