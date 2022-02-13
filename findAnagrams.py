def findAnagrams(s,p):
	L = 0
	R = len(p)-1
	hashForS =[0]*26
	hashForP = [0]*26
	result = []

	for c in p:
		hashForP[ord(c)-97] += 1

	#print('hashForP',hashForP)

	while R < len(s):
		if R == len(p)-1:
			for cc in s[L:R+1]:
				hashForS[ord(cc)-97] += 1
		else:
			hashForS[ord(s[L-1])-97] -= 1
			hashForS[ord(s[R])-97] += 1


		#print(hashForS,L,R)
		if hashForS == hashForP:
			result.append(L)
		L +=1
		R +=1
	return result








s = "abab"
p = "ab"
print(findAnagrams(s,p))