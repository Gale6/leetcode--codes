def findNumberOfLIS(nums):
	dp = {} #key = index, value = [len of LIS, count]
	lenLIS, result = 0, 0 #len of LIS, result = count of LIS

	for i in range(len(nums)-1,-1,-1):
		longestAtI = 1
		countAtI = 1

		for j in range (i+1,len(nums)):
			if nums[i] < nums[j]:
				length, count = dp[j]
				if longestAtI < length + 1:
					longestAtI = length + 1
					countAtI = count
				elif longestAtI == length + 1:
					countAtI += count
		if longestAtI > lenLIS:
			lenLIS = longestAtI
			result = countAtI
		elif longestAtI == lenLIS:
			result += countAtI
		dp[i] = longestAtI,countAtI

	return result

nums = [1,3,5,4,7]
print(findNumberOfLIS(nums))

