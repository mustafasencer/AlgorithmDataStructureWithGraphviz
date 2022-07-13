"""
    On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

    Once you pay the cost, you can either climb one or two steps.
    You need to find minimum cost to reach the top of the floor,
    and you can either start from the step with index 0, or the step with index 1.
"""
from typing import List


def solution(cost: List[int]) -> int:
    min1, min2 = cost[0], cost[1]
    for c in cost[2:]:
        min1, min2 = min2, min(min1, min2) + c
    return min(min1, min2)


def solution_1(cost):
    cost_0, cost_1 = cost[0], cost[1]

    for c in cost[2:]:
        cost_0, cost_1 = cost_1, min(cost_0, cost_1) + c

    return min(cost_0, cost_1)


if __name__ == "__main__":
    nums = [10, 15, 20, 3, 7]
    result = solution_1(nums)
    assert result == 18
    print(result)
