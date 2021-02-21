"""
Find the missing smallest positive integer
"""


def solution(A):
    B = set(A)
    min_value = 1
    for i in range(1, len(A) + 1):
        if i not in B:
            return i
        else:
            min_value = i + 1
    return min_value


if __name__ == '__main__':
    A = [1, 2, 3, 4]
    result = solution(A)
    assert result == 6
    print(result)
