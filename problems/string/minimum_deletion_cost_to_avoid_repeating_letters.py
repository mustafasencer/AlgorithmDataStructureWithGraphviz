"""
https://leetcode.ca/2020-03-26-1578-Minimum-Deletion-Cost-to-Avoid-Repeating-Letters/
https://leetcode.com/problems/minimum-time-to-make-rope-colorful
"""


def solution(string, costs):
    """ """
    min_cost = 0

    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            continue
        if costs[i] > costs[i + 1]:
            current_cost = costs[i]
            next_cost = costs[i + 1]
            costs[i] = min(current_cost, next_cost)
            costs[i + 1] = max(current_cost, next_cost)
        min_cost += costs[i]

    return min_cost


if __name__ == "__main__":
    s = "aabbcc"
    c = [1, 2, 1, 2, 1, 2]
    result = solution(s, c)
    assert result == 3
