"""
Remove duplicates from sorted array without using extra memory
"""

from typing import List


def solution(nums: List[int]) -> int:
	"""
	1. loop over the nums array
	2. use two pointers to track and compare previous value and replace index inplace
	"""
	i = 0

	for item in nums:
		if 0 < i < len(nums) and item == nums[i - 1]:
			nums[i] = item
			continue

		nums[i] = item
		i += 1
	return len(nums[:i])


if __name__ == "__main__":
	result = solution([1, 1, 1, 1, 2, 2, 2, 3, 3, 3])
	assert result == 3
