from typing import List


def solution(nums: List[int]):
	"""
	1. loop over and check the sum equality of both sides of the index
	"""
	for i in range(len(nums)):
		if i == 0:
			sum_first = 0
		else:
			sum_first = sum(nums[:i])
		if sum_first == sum(nums[i + 1 :]):
			return i
	return -1


if __name__ == "__main__":
	nums = [1, 2, 3]
	result = solution(nums)
	assert result == -1
