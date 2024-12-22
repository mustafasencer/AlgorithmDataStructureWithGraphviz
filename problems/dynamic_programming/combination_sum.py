"""
BACKTRACK!

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times! (Important)

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
"""

from typing import List


def solution(candidates: List[int], target: int) -> List[List[int]]:
	result = []
	candidates.sort()
	backtrack(result, candidates, [], target, 0)
	return result


def backtrack(result_, nums, temp, remain, start):
	if remain < 0:
		return
	if remain == 0:
		result_.append(temp)
	else:
		for i in range(start, len(nums)):
			backtrack(result_, nums, temp + [nums[i]], remain - nums[i], i)


def solution_1(candidates, target):
	"""
	1. DFS over the candidates array and check if remain hits 0
	2. Be careful! There can be repeated items in the answer
	3. Thus, line 52 starts from i th index again and again to enable repeated items to be in the result!
	"""
	result = []
	dfs(candidates, target, [], result)
	return result


def dfs(candidates, remain, path, result_):
	if remain < 0:
		return
	if remain == 0:
		result_.append(path)
		return
	for i in range(len(candidates)):
		dfs(candidates[i:], remain - candidates[i], path + [candidates[i]], result_)  # Important!


if __name__ == "__main__":
	result = solution_1([2, 3, 6, 7], 7)
	assert result == [[2, 2, 3], [7]]
