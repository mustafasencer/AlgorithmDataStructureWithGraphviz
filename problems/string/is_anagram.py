"""
Given two strings s and t, return true if t is ananagram of s, and false otherwise.
"""


def solution(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


if __name__ == "__main__":
    result = solution()
    assert result is True
