"""
A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

0 represents a car traveling east,
1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.
"""


# def solution(A):
#     # write your code in Python 3.6
#     index = 0
#     result = []
#     for car in A:
#         index_2 = index
#         if car == 0:
#             while index_2 < len(A):
#                 if A[index_2] == 1:
#                     result.append((index, index_2))
#                 if len(result) > 1000000000:
#                     return -1
#                 index_2 += 1
#         index += 1
#     return len(result)


def solution(A):
    zero_count = 0
    combinations = 0
    for item in A:
        if item == 0:
            zero_count += 1
        else:
            combinations += zero_count

        if combinations > 1e9:
            return -1

    return combinations


def solution_1(A):
    passing_cars = 0
    for i in range(len(A)):
        if A[i] == 0:
            j = i + 1
            while j < len(A):
                if A[j] == 1:
                    passing_cars += 1
                    if passing_cars > 1e9:
                        return -1
                j += 1
    return passing_cars


if __name__ == "__main__":
    A = [0, 1, 0, 1, 1]
    result = solution_1(A)
    assert result == 5
    print(result)
