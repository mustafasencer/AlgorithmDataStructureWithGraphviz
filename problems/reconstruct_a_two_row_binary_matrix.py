"""
https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/
"""


def solution(U, L, C):
    n = len(C)
    upper_row = [0 for _ in range(n)]
    lower_row = [0 for _ in range(n)]

    for i, v in enumerate(C):
        if v == 1:
            if U > L:
                upper_row[i] = 1
                U -= 1
            else:
                lower_row[i] = 1
                L -= 1
        elif v == 2:
            upper_row[i] = lower_row[i] = 1
            U, L = U - 1, L - 1

    if U == L == 0:
        upper_row = "".join(str(e) for e in upper_row)
        lower_row = "".join(str(e) for e in lower_row)
        return ",".join((upper_row, lower_row))
    return "IMPOSSIBLE"


def solution_1(U, L, C):
    upper_row = [0 for _ in range(len(C))]
    lower_row = [0 for _ in range(len(C))]

    for i in range(len(C)):
        if C[i] == 1:
            if U > L:
                U -= 1
                upper_row[i] += 1
            else:
                L -= 1
                lower_row[i] += 1

        elif C[i] == 2:
            U -= 1
            L -= 1
            upper_row[i] += 1
            lower_row[i] += 1

    if U == L == 0:
        return ",".join(
            (
                "".join(str(i) for i in range(len(upper_row))),
                "".join(str(i) for i in range(len(lower_row))),
            )
        )
    return "Not possible"


if __name__ == "__main__":
    U = 3
    L = 2
    C = [2, 1, 1, 0, 1]
    result = solution_1(U, L, C)
    assert result == "11001,10100"
