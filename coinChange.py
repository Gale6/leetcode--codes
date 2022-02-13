def coinChange(coins,amount):

	dp = [float('inf') for i in range (amount + 1)]
	dp[0] = 0

	for i in range(1,amount+1):
		minNumCoins = float('inf')
		for coin in coins:
			if coin <= i:
				if dp[i-coin] != float('inf'):
					minNumCoins = min(minNumCoins,1 + dp[i-coin])
		dp[i] = minNumCoins
	if dp[amount] != float('inf'):
		return dp[amount]
	else:
		return -1

coins = [1,2,5]
amount = 11

print(coinChange(coins,amount))