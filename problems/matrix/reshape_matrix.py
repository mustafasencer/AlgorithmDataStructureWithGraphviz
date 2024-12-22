"""
https://leetcode.com/problems/reshape-the-matrix/
"""


def solve(mat, r, c):
	count = r * c
	if count != sum(1 for row in mat for _ in row):
		return mat

	result = []
	flatten_mat = [col for row in mat for col in row]
	for i in range(r):
		row = []
		for j in range(c):
			row.append(flatten_mat.pop(0))
		result.append(row)

	return result


if __name__ == "__main__":
	mat = [[1, 2], [3, 4]]
	r = 1
	c = 4
	result = solve(mat, r, c)
	assert result == ""
