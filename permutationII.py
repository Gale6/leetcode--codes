def permuteUnique(nums):
	result = []
	possible = []
	hashmap = { n : 0 for n in nums}
	for n in nums:
		hashmap[n] += 1


	print('hashmap',hashmap)
	def dfs(j):
		if j == len(nums):
			result.append(possible.copy())
		else:
			for h in hashmap:
				if hashmap[h] != 0:					
					possible.append(h)
					hashmap[h] -= 1
					dfs(j+1)
					hashmap[h] += 1
					possible.pop()
	dfs(0)
	return result






nums = [1,1,2,2]

print(permuteUnique(nums))
