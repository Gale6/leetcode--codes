def subsetsII(nums):
	result = []
	subsets = []

	# have to sort it!!
	nums.sort()
	def dfs(i):
		if i >= len(nums):
			result.append(subsets.copy())
			return

		subsets.append(nums[i])


		#print(i,'be',subsets)

		dfs(i+1)

		subsets.pop()
		#print(i,'af',subsets)


		while i + 1 < len(nums) and nums[i] == nums[i+1]:
			i += 1

		dfs(i+1)

	dfs(0)

	return result
nums = [1,2,2,3]
print(subsetsII(nums))