from typing import List


def solve(nums: List[int]) -> List[List[int]]:
	"""
	1. Backtracking approach to find all possible permutations
	"""

	def backtrack(start, end):
		if start == end:
			ans.append(nums[:])
		for i in range(start, end):
			nums[start], nums[i] = nums[i], nums[start]
			backtrack(start + 1, end)
			nums[start], nums[i] = nums[i], nums[start]

	ans = []
	backtrack(0, len(nums))
	return ans


def solve_2(nums: List[int]) -> List[List[int]]:
	"""
	1. DFS approach to find all possible permutations
	"""

	def dfs(nums, path, res):
		if not nums:
			res.append(path)
		for i in range(len(nums)):
			dfs(nums[:i] + nums[i + 1 :], path + [nums[i]], res)

	res = []
	dfs(nums, [], res)
	return res


if __name__ == "__main__":
	nums = [1, 2, 3]
	result = solve_2(nums)
	assert result == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
