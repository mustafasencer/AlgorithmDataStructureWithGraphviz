def solution(A) -> bool:
    average = sum(A) // 3
    remainder = sum(A) % 3
    count = 0
    part = 0
    for a in A:
        part += a
        if part == average:
            count += 1
            part = 0

    return not remainder and count >= 3


if __name__ == '__main__':
    A = [1, -1, 1, -1]
    result = solution(A)
    assert result == False
    print(result)
