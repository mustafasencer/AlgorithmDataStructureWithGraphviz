from typing import List


def solution(nums: List[int], k: int) -> List[int]:
	length = len(nums)
	result = []

	for i in range(length - k, 2 * length - k):
		i = i % length
		result.append(nums[i])

	return result


def solution_1(nums, k):
	"""
	1. modify nums in-place instead.
	"""
	l = len(nums)
	k = k % l
	nums[:] = nums[l - k :] + nums[: l - k]
	return nums


def solution_2(nums, k):
	result = [0] * len(nums)
	for i in range(len(nums)):
		result[(i + k) % len(nums)] = nums[i]
	return result


def solution_3(nums, k):
	i = 0
	start = 0
	value = nums[start]
	while i < len(nums):
		next_index = (start + k) % len(nums)
		temp = nums[next_index]
		nums[next_index] = value
		value = temp
		start = next_index
		i += 1
	return nums


if __name__ == "__main__":
	nums = [1, 2, 3, 4, 5, 6, 7]
	k = 3
	result = solution_1(nums, k)
	assert nums == result
