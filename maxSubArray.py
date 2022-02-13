def maxSubArray(nums):
	result = nums[0]
	currSum = 0

	for n in nums:
		if currSum < 0:
			currSum = 0 

		currSum = currSum + n
		result = max(result,currSum)

	return result