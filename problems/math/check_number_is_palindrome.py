"""
To check a number is palindrome or not without using any extra space
https://www.geeksforgeeks.org/check-number-palindrome-not-without-using-extra-space/
"""


def solution(number: int) -> bool:
    divisor = 1

    while number / divisor >= 10:
        divisor *= 10

    while number > 0:
        print(divisor)
        leading_value = number // divisor
        trailing_value = number % 10

        if leading_value != trailing_value:
            return False

        number = (number % divisor) // 10

        divisor //= 100

    return True


if __name__ == "__main__":
    number = 12211
    result = solution(number)
    assert result is False
    print(result)
