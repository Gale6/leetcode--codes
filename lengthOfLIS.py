def lengthOfLIS(nums):
	dp = [1]*len(nums)
	for i in range(1,len(nums)):
		longestSoFar = 1
		for j in range(i):
			if nums[i] > nums[j]:
				longestSoFar = max(longestSoFar,1+dp[j])
		dp[i] = longestSoFar
	return max(dp)



nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))
