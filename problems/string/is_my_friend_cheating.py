"""
Codewars
"""


def remove_nb(n):
	sum = n * (n + 1) / 2

	def _apply():
		for a in range(1, n + 1):
			b = (sum - a) / (a + 1)
			if b.is_integer() and b <= n:
				yield (a, int(b))

	result = _apply()
	return list(result)


if __name__ == "__main__":
	result = remove_nb(5)
	print(result)
