def permutation(nums):
	result = []
	def backtracking(nums,used,l):
		if len(nums) == len(l):
			result.append(l.copy())
			return
		else:
			for i in range (len(nums)):
				if i not in used:
					l.append(nums[i])
					used.append(i)
					print(used,l)
					backtracking(nums,used,l)
					used.pop()
					l.pop()
	backtracking(nums,[],[])
	return result
print(permutation([1,2,3]))