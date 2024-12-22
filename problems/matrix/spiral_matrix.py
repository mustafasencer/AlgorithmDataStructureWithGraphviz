from typing import List


class Solution:
	def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
		if not matrix:
			return []
		result = []
		n = len(matrix)
		m = len(matrix[0])
		up = left = 0
		down = n - 1
		right = m - 1

		while up <= down and left <= right:
			for i in range(left, right + 1):
				result.append(matrix[up][i])
			up += 1

			for j in range(up, down + 1):
				result.append(matrix[j][right])

			right -= 1

			if up <= down:
				for i in range(right, left - 1, -1):
					result.append(matrix[down][i])

			down -= 1

			if left <= right:
				for i in range(down, up - 1, -1):
					result.append(matrix[i][left])
			left += 1

		return result

	def spiralOrder_(self, matrix):
		return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])


if __name__ == "__main__":
	result = Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
	print(result)
