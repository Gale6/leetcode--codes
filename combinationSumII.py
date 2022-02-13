def combinationSum(candidates,target):
	result = []
	possible = []

	candidates.sort()
	def dfs(i,currSum):	
		if currSum == target:
			result.append(possible.copy())
			return
		if i >= len(candidates) or currSum > target:
			return	

		possible.append(candidates[i])
		dfs (i + 1, currSum + candidates[i])
		possible.pop()

		while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
			i += 1

		dfs(i + 1,currSum)

	dfs(0,0)

	return result


candidates = [10,1,2,7,6,1,5]
target = 8

print(combinationSum(candidates,target))