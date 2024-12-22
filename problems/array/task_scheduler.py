"""
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task.
Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete
either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks
(the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.
"""

import collections
from heapq import heappop, heappush


def solution(tasks: list[str], n: int) -> int:
    curr_time, h = 0, []
    for k, v in collections.Counter(tasks).items():
        heappush(h, (-1 * v, k))
    while h:
        i, temp = 0, []
        while i <= n:
            curr_time += 1
            if h:
                x, y = heappop(h)
                if x != -1:
                    temp.append((x + 1, y))
            if not h and not temp:
                break
            i += 1
        for item in temp:
            heappush(h, item)
    return curr_time


if __name__ == "__main__":
    tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
    n = 2
    result = solution(tasks, n)
    assert result == 16
