"""
Given an array A[] of integers, write a program to find the maximum difference between
any two elements such that the larger element appears after the smaller element.
In other words, we need to find max(A[j] - A[i]), where A[j] > A[i] and j > i.
"""


def solution(nums: list[int]):
    pass


if __name__ == "__main__":
    nums = [1, 2, 4, 9, 5, 3]
    result = solution(nums)
    assert result == 8
