def is_palindrome(s: str) -> bool:
    s = s.lower()
    i = 0
    j = len(s) - 1
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1

        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def test(string: str) -> bool:
    string = string.lower()
    left = 0
    right = len(string) - 1

    while left < right:
        while left < right and string[left].isalnum():
            left += 1
        while left < right and string[left].isalnum():
            right -= 1

        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    result = test("0P")
