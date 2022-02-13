def backspaceCompare(s,t):
	pointerS = len(s) -1
	pointerT = len(t) -1

	numOfBS = 0
	numOfBT = 0

	while pointerS >= 0 or pointerT >= 0:
		while pointerS >= 0 and (s[pointerS] == '#' or numOfBS > 0):
			if s[pointerS]=='#':
				numOfBS += 1
			else:
				numOfBS -= 1
			pointerS -= 1


		while pointerT >= 0 and (t[pointerT] == '#' or numOfBT > 0):
			if t[pointerT]=='#':
				numOfBT += 1
			else:
				numOfBT -= 1
			pointerT -= 1

		if pointerS >=0 and pointerT >=0:
			if s[pointerS] != t[pointerT] :
				return False
			else:
				pointerT -= 1
				pointerS -= 1
		else:
			if pointerS >=0 or pointerT >=0:
				return False


	return True

a = "bxj##tw"
b = "bxo#j##tw"

print(backspaceCompare(a,b))