"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.
"""


def solution(A):
    result = []

    for i in range(len(A)):
        A.pop(0)
        if not A:
            result.append(-1)
        else:
            result.append(max(A))
    return result


def solution_2(A):
    mx = -1
    for i in range(len(A) - 1, -1, -1):
        A[i], mx = mx, max(mx, A[i])
    return A


def test(A):
    for i in range(len(A)):
        if i == len(A) - 1:
            value = -1
        else:
            value = max(A[i + 1:])
        A[i] = value

    return A


def solution_3(A):
    i = 0

    for j in range(1, len(A) + 1):
        if i == len(A) - 1:
            A[i] = -1
            break
        A[i] = max(A[j:])
        i += 1

    return A


if __name__ == '__main__':
    A = [21, 18, 5, 4, 6, 1]
    result = solution_3(A)
    assert result == [18, 6, 6, 6, 1, -1]
    print(result)
