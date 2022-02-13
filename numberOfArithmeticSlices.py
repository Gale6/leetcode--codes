def numberOfArithmeticSlices(nums):
	result = 0
	N = len(nums)
	dp = [None] * (N - 1)
	for i in range (len(dp)):
		dp[i] = nums[i+1] - nums[i]
	print(dp)
	l,r = 0,1 
	arithmeticCounter = 1
	while r < len(dp):
		if dp[l] == dp[r]:
			result += arithmeticCounter
			arithmeticCounter += 1
			r += 1
		else:
			arithmeticCounter = 1
			l = r
			r = l + 1
	return result



nums = [1]
print(numberOfArithmeticSlices(nums))