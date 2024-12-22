def solution(coins, amount):
	MAXs = [1e9] * amount
	dp = [0] + MAXs
	for i in range(1, amount + 1):
		for coin in coins:
			if i - coin >= 0:
				dp[i] = min(dp[i], dp[i - coin] + 1)
	if dp[-1] == 1e9:
		return -1
	return dp[-1]


def solution_1(coins, amount):
	if amount == 0:
		return 0
	value1 = [0]
	value2 = []
	nc = 0
	visited = [False] * (amount + 1)
	visited[0] = True
	while value1:
		nc += 1
		for v in value1:
			for coin in coins:
				newval = v + coin
				if newval == amount:
					return nc
				elif newval > amount:
					continue
				elif not visited[newval]:
					visited[newval] = True
					value2.append(newval)
		value1, value2 = value2, []
	return -1


def solution_2(coins, amount):
	result = []
	counter = 0

	def dfs(coins, remain, ans, result):
		nonlocal counter
		counter += 1
		print(counter)
		if remain < 0:
			return
		if remain == 0:
			return result.append(ans)
		if not coins:
			return

		for i in range(len(coins)):
			dfs(coins[i:], remain - coins[i], ans + [coins[i]], result)

	dfs(coins, amount, [], result)
	return min([len(i) for i in result])


if __name__ == "__main__":
	coins = [1, 2, 5]
	amount = 6
	result = solution_2(coins, amount)
	assert result == 2
