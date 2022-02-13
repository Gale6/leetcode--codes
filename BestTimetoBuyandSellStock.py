def maxProfit(price):
	result = 0
	l,r = 0

	while r < len(price):
		if price[l] <= price[r]:
			result = max(result, price[r] - price[l])
		else:
			l = r
		r += 1
			
	return result