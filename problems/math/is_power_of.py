"""Fill in the blanks to make the is_power_of function return whether the number is a power of the given base.
Note: base is assumed to be a positive number. Tip: for functions that return a boolean value, you can return the result of a comparison."""


def solution(n: int, b: int) -> bool:
    if n == b:
        return True

    if n % b != 0:
        return False

    return solution(n // b, b)


if __name__ == "__main__":
    result = solution(8, 2)
    print(result)
