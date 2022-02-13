def maxProduct(nums):
	curMin,curMax = 1,1
	result = max(nums)
	for n in nums:
		tempMin = n * curMin
		tempMax = n * curMax
		curMin = min(tempMax,tempMin,n)
		curMax = max(tempMax,tempMin,n)
		result = max(curMax,result)
	return result