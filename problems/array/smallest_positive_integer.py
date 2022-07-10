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


def sol_2(A):
    distinct = set(A)
    min_value = 1
    for _ in A:
        if min_value not in distinct:
            return min_value
        min_value += 1
    return min_value


if __name__ == "__main__":
    A = [1, 2, 3, 4]
    result = sol_2(A)
    assert result == 5
    print(result)
