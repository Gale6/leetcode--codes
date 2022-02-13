def productExceptSelf(nums):
	pre = 1
	result = [1]
	for i in range (len(nums)-1):
		pre = pre * nums[i]
		result.append(pre)
	post = 1
	for j in range(len(nums)-1,0,-1):
		post = post * nums[j]
		result[j-1] = post * result[j-1]
	return result



nums = [1,2,3,4]
print(productExceptSelf(nums))