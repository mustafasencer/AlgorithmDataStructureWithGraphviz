def solve(number: int):
    if number == 0:
        return 0
    if number == 1:
        return 1
    return solve(number - 1) + solve(number - 2)


def solve_2(number: int) -> int:
    a = 0
    b = 1

    while a <= number:
        c = a + b
        a = b
        b = c

    return b


if __name__ == '__main__':
    number = 7
    result = solve_2(number)
    assert result == 13
