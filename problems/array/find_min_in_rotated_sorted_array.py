"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.
"""

from typing import List


def find_min(nums: List[int]) -> int:
	"""
	1. take a binary search approach as the array is sorted
	2. try to find the lowest element possible
	"""
	low = 0
	high = len(nums) - 1

	while low < high:
		mid = int((high + low) / 2)
		if nums[mid] > nums[high]:
			low = mid + 1
		else:
			high = mid

	return nums[low]


if __name__ == "__main__":
	result = find_min([3, 4, 5, 0, 1, 2])
	print(result)
