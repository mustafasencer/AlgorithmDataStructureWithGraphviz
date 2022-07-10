def solve(n, a=1):
    if n == 0:
        return a

    return solve(n - 1, a * n)


def solve_2(n, s=0):
    if n == 0:
        return s

    return solve_2(n - 1, s + n)


def solve_3(n, a=0, b=1):
    if n == 0:
        return a
    return solve_3(n - 1, b, a + b)


if __name__ == "__main__":
    result = solve(4)
    result_2 = solve_2(4)
    result_3 = solve_3(4)
    assert result == 24
    assert result_2 == 10
    assert result_3 == 3
