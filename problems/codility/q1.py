"""
https://leetcode.ca/2020-03-26-1578-Minimum-Deletion-Cost-to-Avoid-Repeating-Letters/
https://leetcode.com/problems/minimum-time-to-make-rope-colorful
"""


def solution(S, C):
    # write your code in Python 3.6

    min_cost = 0

    for i in range(len(S) - 1):
        if S[i] != S[i + 1]:
            continue
        if C[i] > C[i + 1]:
            current_cost = C[i]
            next_cost = C[i + 1]
            C[i] = min(current_cost, next_cost)
            C[i + 1] = max(current_cost, next_cost)
        min_cost += C[i]

    return min_cost


if __name__ == "__main__":
    s = "aabbcc"
    c = [1, 2, 1, 2, 1, 2]
    result = solution(s, c)
    assert result == 3
