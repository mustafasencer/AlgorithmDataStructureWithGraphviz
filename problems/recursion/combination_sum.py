"""
BACKTRACK!

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times! (Important)

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

"""


def solution(candidates: list[int], target: int) -> list[list[int]]:
    result = []
    candidates.sort()

    def backtrack(result_, nums, temp, remain, start) -> None:
        if remain < 0:
            return
        if remain == 0:
            result_.append(temp)
        else:
            for i in range(start, len(nums)):
                backtrack(result_, nums, [*temp, nums[i]], remain - nums[i], i)

    backtrack(result, candidates, [], target, 0)
    return result


def solution_v2(candidates, target):
    """
    1. DFS over the candidates array and check if remain hits 0
    2. Be careful! There can be repeated items in the answer
    3. Thus, line 52 starts from i th index again and again to enable repeated items to be in the result!
    """
    result = []

    def dfs(candidates, path, remain):
        nonlocal result
        if remain < 0:
            return
        if remain == 0:
            result.append(path)

        for i in range(len(candidates)):
            dfs(candidates[i:], [*path, candidates[i]], remain - candidates[i])

    dfs(candidates, [], target)
    return result


if __name__ == "__main__":
    result = solution_v2([2, 3, 6, 7], 7)
    assert result == [[2, 2, 3], [7]]
