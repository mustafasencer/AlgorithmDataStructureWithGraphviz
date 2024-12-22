from typing import List


def solve(matrix: List[List[int]]):
	"""
	1. start from the 2nd row!
	2. check the previous row within the diagonal limits
	3. change the current i, j item in the matrix by setting the min sum value
	4. the last row of the matrix should have the last results and min should be selected
	"""
	for i in range(1, len(matrix)):
		for j in range(len(matrix[i])):
			prev_row = matrix[i - 1][max(0, j - 1) : min(j + 2, len(matrix[i]))]
			matrix[i][j] = min([item + matrix[i][j] for item in prev_row])

	return min(matrix[-1])


if __name__ == "__main__":
	matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
	result = solve(matrix)
	assert result == 13
