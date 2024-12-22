"""
https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/
"""


def solve(n, k):
	result = ["a"] * n
	remaining = k - n

	idx = n - 1
	while remaining > 0:
		if remaining > 25:
			result[idx] = "z"
			remaining -= 25
		else:
			result[idx] = chr(96 + remaining + 1)
			remaining = 0
		idx -= 1
	return "".join(result)


if __name__ == "__main__":
	n, k = 3, 27
	result = solve(n, k)
	assert result == "aay"
