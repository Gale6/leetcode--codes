def combine(n,k):
	result = []

	def backtracking(n,k,result,begin,l):
		if len(l) == k:
			result.append(l.copy())
			return
		else:
			for i in range(begin,n + 1):
				l.append(i)
				backtracking(n,k,result,i + 1,l)
				l.pop()
	print('HIHiHIH')
	backtracking(n,k,result,1,[])
	return result

print(combine(4,2))