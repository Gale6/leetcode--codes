def subsets(nums):
	result = []
	subsets = []


	def dfs(i):
		if i >= len(nums):
			result.append(subsets.copy())
			return

		subsets.append(nums[i])


		#print(i,'be',subsets)

		dfs(i+1)

		subsets.pop()
		#print(i,'af',subsets)

		dfs(i+1)

	dfs(0)

	return result
nums = [1,2,3]
print(subsets(nums))