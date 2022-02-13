def numSubarrayProductLessThanK(nums,k):

	if k <=1:
		return 0
	L = 0
	R = 0
	result = 0
	product = 1
	while R < len(nums):
		product *= nums[R]

		while product>= k:
			product /= nums[L]
			L += 1

		result += R - L + 1

		R += 1
	return result


nums = [10,5,2,6]
k = 100
print(numSubarrayProductLessThanK(nums,k))