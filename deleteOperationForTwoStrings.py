def minDistance(word1,word2):
	dp = []
	for i in range(len(word1)+1):
		dp.append([])
		for j in range (len(word2)+1):
			dp[i].append(0)

	for x in range(len(word1)-1,-1,-1):
		for y in range(len(word2)-1,-1,-1):
			if word1[x] == word2[y]:
				dp[x][y] = 1 + dp[x+1][y+1]
			else:
				dp[x][y] = max(dp[x][y+1],dp[x+1][y])

	result = (len(word1) - dp[0][0]) + (len(word2) - dp[0][0])
	return result



word1 = "sea"
word2 = "eat"

print(minDistance(word1,word2))