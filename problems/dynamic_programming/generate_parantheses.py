"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
https://leetcode.com/problems/generate-parentheses/discuss/10110/Simple-Python-DFS-solution-with-explanation
https://leetcode.com/problems/generate-parentheses/discuss/10369/Clean-Python-DP-Solution.
"""


def solution(n: int):
    left, right = n, n
    result = []

    def dfs(left, right, path) -> None:
        nonlocal result
        if right < left:
            return
        if not left and not right:
            result.append(path)
            return
        if left:
            dfs(left - 1, right, path + "(")
        if right:
            dfs(left, right - 1, path + ")")

    dfs(left, right, "")
    return result


def dp(n: int):
    pass


if __name__ == "__main__":
    n = 3
    result = solution(n)
    assert result == ["((()))", "(()())", "(())()", "()(())", "()()()"]
