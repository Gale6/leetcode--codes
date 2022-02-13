def minSubArrayLen(target,nums):
	L = 0
	R = 0
	currSum = 0
	currMin = float('inf')


	while R < len(nums):
		currSum += nums[R]

		while currSum >= target:
			currMin = min(currMin,R-L+1)
			currSum -= nums[L]
			L += 1

		R += 1
	if currMin == float('inf'):
		return 0
	else:
		return currMin


target = 7
nums = [2,3,1,2,4,3]
print(minSubArrayLen(target,nums))
