def letterCasePermutation(s):
	result = []
	def backtracking(s,begin,s2):
		if len(s) == len(s2):
			result.append(s2)
			return
		else:
			if s[begin].isdigit():
				s2 = s2 + s[begin]
				backtracking(s,begin+1,s2)
				s2 = s2[0:begin]
			else:
				s2 = s2 + s[begin].lower()
				backtracking(s,begin+1,s2)
				s2 = s2[0:begin]
				s2 = s2 + s[begin].upper()
				backtracking(s,begin+1,s2)
				s2 = s2[0:begin]
	backtracking(s,0,'')
	return result

print(letterCasePermutation("a1b2"))