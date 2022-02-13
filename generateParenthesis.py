def generateParenthesis(n):
	result = []

	def dfs(possible,openP,closeP):

		if closeP == 0:
			result.append(possible)
		else:
			if openP > 0:
				dfs(possible + '(',openP - 1, closeP)
			if openP < closeP:
				dfs(possible + ')', openP, closeP - 1)
	dfs('',n,n)

	return result

temp = generateParenthesis(4)
print(temp,len(temp))