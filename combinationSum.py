def combinationSum(candidates,target):
	result = []
	possible = []


	def dfs(i,currSum):	
		if currSum == target:
			result.append(possible.copy())
			return
		if i >= len(candidates) or currSum > target:
			return	

		possible.append(candidates[i])
		dfs (i, currSum + candidates[i])
		possible.pop()
		dfs(i+1,currSum)

	dfs(0,0)

	return result


candidates = [2,3,6,7]
target = 7

print(combinationSum(candidates,target))