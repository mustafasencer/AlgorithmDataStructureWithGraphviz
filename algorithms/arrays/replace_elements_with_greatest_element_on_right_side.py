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


if __name__ == '__main__':
    A = [21, 18, 5, 4, 6, 1]
    result = solution_2(A)
    assert result == [18, 6, 6, 6, 1, -1]
    print(result)
