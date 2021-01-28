def solution(N):
    max_gap = 0
    count = 0
    binary = f'{N:08b}'
    initialized = 0

    for char in binary:

        if char == "1":
            initialized = 1
            max_gap = max(max_gap, count)
            count = 0

        elif char == "0":
            if initialized:
                count += 1

    return max_gap


if __name__ == '__main__':
    N = 32
    result = solution(N)
    assert result == 0
    print(result)
