def solve(number):
    """1. (n - 1) ^ 2 = n ^ 2 - 2 * n + 1."""
    if number == 0:
        return 0
    return solve(number - 1) + 2 * number - 1


if __name__ == "__main__":
    number = 5
    result = solve(number)
    assert result == 25
