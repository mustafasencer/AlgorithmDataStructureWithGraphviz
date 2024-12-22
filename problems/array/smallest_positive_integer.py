"""
Find the missing smallest positive integer
"""


def solution(nums):
	"""
	1. should return 1 if not present
	2. if not just loop over the nums array find the first positive integer lacking
	"""
	B = set(nums)
	min_value = 1
	for i in range(1, len(nums) + 1):
		if i not in B:
			return i
		else:
			min_value = i + 1
	return min_value


def solution_1(nums):
	distinct = set(nums)
	min_value = 1
	for _ in nums:
		if min_value not in distinct:
			return min_value
		min_value += 1
	return min_value


if __name__ == "__main__":
	nums = [1, 2, 3, 4]
	result = solution_1(nums)
	assert result == 5
