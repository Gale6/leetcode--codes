def numDecodings(s):
	if s[0] =='0' or not s:
		return 0

	dp = [1] * len(s)
	if s[len(s)-1] == '0':
		dp[len(s)-1] = 0
	else:
		dp[len(s)-1] = 1
	if s[len(s)-2] == '0':
		dp[len(s)-2] = 0
	else:
		dp[len(s)-2] = 1
		if int(s[len(s)-2:len(s)]) <= 26:
			dp[len(s)-2] += 1


	for i in range(len(s)-2,-1,-1):
		if dp[i] == '0':
			dp[i] = 0
		else:
			dp[i] = dp[i+1]
			if int(s[i:i+2]) <= 26:
				dp[i] += dp[i+2]

	return dp[0]




print(numDecodings('1l2'))
