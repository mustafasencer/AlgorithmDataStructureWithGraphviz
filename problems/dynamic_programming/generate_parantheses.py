"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
https://leetcode.com/problems/generate-parentheses/discuss/10110/Simple-Python-DFS-solution-with-explanation
https://leetcode.com/problems/generate-parentheses/discuss/10369/Clean-Python-DP-Solution.
"""


def solve(n: int):
    left, right = n, n
    result = []
    dfs(left, right, "", result)
    return result


def dfs(left, right, path, result) -> None:
    if right < left:
        return
    if not left and not right:
        result.append(path)
        return
    if left:
        dfs(left - 1, right, path + "(", result)
    if right:
        dfs(left, right - 1, path + ")", result)


if __name__ == "__main__":
    n = 5
    result = solve(n)
    assert result == ["((()))", "(()())", "(())()", "()(())", "()()()"]
