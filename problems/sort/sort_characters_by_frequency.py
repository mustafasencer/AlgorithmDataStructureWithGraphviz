"""
https://leetcode.com/problems/sort-characters-by-frequency/
"""

from collections import Counter


def solve(s: str) -> str:
    return "".join([k * v for k, v in Counter(s).most_common()])


if __name__ == "__main__":
    s = "Aaaaaaabb"
    result = solve(s)
    print(result)
