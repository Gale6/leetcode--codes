def longestCommonSubsequence(text1,text2):
	dp = []
	for i in range(len(text1)+1):
		dp.append([])
		for j in range (len(text2)+1):
			dp[i].append(0)

	for x in range(len(text1)-1,-1,-1):
		for y in range(len(text2)-1,-1,-1):
			if text1[x] == text2[y]:
				dp[x][y] = 1 + dp[x+1][y+1]
			else:
				dp[x][y] = max(dp[x][y+1],dp[x+1][y])

	return dp[0][0]





text1 ="horse"
text2 ="ros"
print(len(text1))
print(longestCommonSubsequence(text1,text2))
