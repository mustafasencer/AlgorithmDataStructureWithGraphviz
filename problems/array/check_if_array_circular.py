from typing import List


def solution(nums: List[int]) -> bool:
	"""
	1. loop over the array
	2. check if any index has a circular path
	3. is_seen stores the indices that have been seen
	4. if local set has the index stored then the circularity is confirmed
	"""
	is_seen = set()

	for i in range(len(nums)):
		local = set()

		while True:
			if i in local:
				return True

			if i in is_seen:  # means that we have already been this path and it is not circular
				break

			is_seen.add(i)
			local.add(i)

			prev = i
			i = (i + nums[i]) % len(
				nums
			)  # Add the value at index i and get the mod of it to find the next i in the path
			if (
				prev == i or (nums[i] > 0) != (nums[prev] > 0)
			):  # if current i ends up in the same i than no path (single item) and both the i and prev values are > 0
				break

	return False


if __name__ == "__main__":
	nums = [2, 3, 1, 4, 0]
	result = solution(nums)
	assert result is True
