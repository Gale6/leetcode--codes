def shortestPathBinaryMatrix(grid):
	if grid[0][0] != 0 or grid[len(grid)-1][len(grid[len(grid)-1])-1] != 0:
		return -1
	directionMatrix = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
	visited = []
	for i in range(len(grid)):
		visited.append([])
		for j in range(len(grid[i])):
			visited[i].append(False)
	visited[len(grid)-1][len(grid[len(grid)-1])-1] = 1
	workingQueue = [[len(grid)-1, len(grid[len(grid)-1])-1]]
	
	while len(workingQueue) != 0:
		temp = workingQueue.pop(0)
		for direct in directionMatrix:
			nr,nc = temp[0] + direct[0], temp[1] + direct[1]
			if 0 <= nr and nr < len(grid) and 0 <= nc and nc < len(grid[nr]) and grid[nr][nc] == 0 and visited[nr][nc] == False:
				visited[nr][nc] = visited[temp[0]][temp[1]] + 1
				workingQueue.append([nr,nc])
	print(visited)
	if visited[0][0] == False:
		return -1 
	else: 
		return visited[0][0]



grid = [[0,0,0],[1,0,0],[1,1,0]]


print(shortestPathBinaryMatrix(grid))

