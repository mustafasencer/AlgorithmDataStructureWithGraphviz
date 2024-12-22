"""
Partition array into three parts with equal sum
"""


def solution(nums) -> bool:
	"""
	1. loop over the nums array
	2. add item value to the part sum and check if part sum has reached the average (1/3)
	3. return True if the count is 3
	"""
	average = sum(nums) // 3
	remainder = sum(nums) % 3
	count = 0
	part = 0
	for a in nums:
		part += a
		if part == average:
			count += 1
			part = 0

	return not remainder and count >= 3


if __name__ == "__main__":
	A = [1, -1, 1, -1, 1, -1]
	result = solution(A)
	assert result is True
