def uniquePaths(m,n):
	dpMatrix = []
	for i in range (m):
		dpMatrix.append([])
		for x in range (n):
			dpMatrix[i].append(0)
	for j in range(n):
		dpMatrix[0][j] = 1
	for k in range(m):
		dpMatrix[k][0] = 1
	for x in range(1,m):
		for y in range(1,n):
			dpMatrix[x][y] = dpMatrix[x-1][y] + dpMatrix[x][y-1]
	print(dpMatrix)
	return dpMatrix[m-1][n-1]
print(uniquePaths(3,7))
