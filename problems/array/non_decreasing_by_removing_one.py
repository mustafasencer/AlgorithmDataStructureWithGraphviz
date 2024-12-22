def solution(nums):
	"""
	1. loop over the nums array
	2. remove in each iteration the current indexed item and check if it is sorted
	3. return True if it is the case, False if not
	"""
	if nums == sorted(nums):
		return True

	for i in range(len(nums)):
		remove = nums[:i] + nums[i + 1 :]
		if remove == sorted(remove):
			return True
	return False


if __name__ == "__main__":
	nums = [1, 4, 2, 3]
	result = solution(nums)
	assert result is True
