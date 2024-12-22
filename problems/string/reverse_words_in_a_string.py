"""Reverse Words in a String."""


def solution(string: str):  # not working right now, should be revised! (inplace trial)
    string = string.strip()
    word_start = len(string)
    word_end = len(string)
    to_add = False
    for i in range(len(string) - 1, -1, -1):
        if string[i].isspace():
            continue
        if string[i].isalnum() and i + 1 < len(string) and string[i + 1].isspace():
            word_end = i

        if string[i].isalnum() and i - 1 >= 0 and string[i - 1].isspace():
            to_add = True
            word_start = i

        if to_add:
            string = string[word_start:word_end] + " " + string[:word_start]
            to_add = False
    return string


def solution_1(string: str):
    return " ".join(string.strip().split()[::-1])


if __name__ == "__main__":
    string = "  Bob    Loves  Alice   "
    result = solution_1(string)
    assert result == "Alice Loves Bob"
