def generateParenthesis(n):
	result = []


	def dfs(n,possible,edge):

		if n == 0:
			result.append(possible)
			result.append(edge)
		else:
			if possible != '':
				for c in range (len(possible)):
					if possible[c] == ')':
						dfs(n-1, possible[:c] + '()' + possible[c:],possible + '()')

				#dfs(n-1,possible + '()')


			else:
				dfs(n-1,'()','()')
	dfs(4,'','')
	return result

temp = generateParenthesis(4)
print(temp,len(temp))