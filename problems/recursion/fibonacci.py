def solve(number: int):
    if number == 0:
        return 0
    if number == 1:
        return 1
    return solve(number - 1) + solve(number - 2)


def solve_2(number: int) -> int:
    a = 0
    b = 1
    n = 1

    while n < number:
        c = a + b
        a = b
        b = c
        n += 1

    return b


if __name__ == "__main__":
    number = 4
    result = solve_2(number)
    assert result == 3
