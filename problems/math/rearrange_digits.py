def solution(digits):
    divisor = 10 ** (len(str(digits)) - 1)
    remaining = 10
    result = ""

    while divisor >= remaining:
        first = digits // divisor
        last = digits % remaining

        result += str(first)[-1]
        result += str(last)[0]

        divisor //= 10
        remaining *= 10

    return int(result)


if __name__ == "__main__":
    digits = 12345678
    result = solution(digits)
    assert result == 18273645
