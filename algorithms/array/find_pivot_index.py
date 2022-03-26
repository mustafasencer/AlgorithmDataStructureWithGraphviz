"""

"""
from typing import List


def solution(A: List[int]):
    for i in range(len(A)):
        if i == 0:
            sum_first = 0
        else:
            sum_first = sum(A[:i])
        if sum_first == sum(A[i + 1:]):
            return i
    return -1


if __name__ == '__main__':
    A = [1, 2, 3]
    result = solution(A)
    assert result == -1
    print(result)
