def letterCombinations(digits):
	hashMap = {
	'2':'abc',
	'3':'def',
	'4':'ghi',
	'5':'jkl',
	'6':'mno',
	'7':'pqrs',
	'8':'tuv',
	'9':'wxyz'
	}

	result = []
	if len(digits) == 0:
		return result

	def dfs(i,possible):
		if i == len(digits):
			result.append(possible)
		else:
			for j in hashMap[digits[i]]:
				dfs(i+1,possible + j)
	dfs(0,'')
	return result


digits = '23'
print(letterCombinations(digits))