def minimumTotal(triangle):
	pathResult = []
	for i in range(len(triangle)):
		pathResult.append([])
		for j in range(len(triangle[i])):
			pathResult[i].append(float('inf'))
	for m in range(len(triangle[len(triangle)-1])):

		pathResult[len(triangle)-1][m] = triangle[len(triangle)-1][m]

	for x in range(len(triangle)-2,-1,-1):
		for y in range(len(triangle[x])-1,-1,-1):
			pathResult[x][y] = min(pathResult[x+1][y],pathResult[x+1][y+1]) + triangle[x][y]
			print(x,y)

	return pathResult[0][0]













#print(minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
#print(minimumTotal([[-10]]))
print(minimumTotal([[-1],[2,3],[1,-1,-3]]))