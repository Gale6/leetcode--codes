def numIslands(grid):
	result = 0
	visitedGrid = []

	directionMatrix = [[-1,0],[1,0],[0,-1],[0,1]]
	for i in range(len(grid)):
		visitedGrid.append([])
		for j in range (len(grid[i])):
			visitedGrid[i].append('false')

	#print(visitedGrid)

	def bfs(grid,visitedGrid,r,c):
		visitedGrid[r][c] = 'true'
		if grid[r][c] == "1":			
			for direct in directionMatrix:
				nr = r + direct[0]
				nc = c + direct[1]

				if 0 <= nr and nr < len(grid) and 0 <= nc and nc < len(grid[nr]):
					if visitedGrid[nr][nc] == "false":
						bfs(grid,visitedGrid,nr,nc)

	for x in range(len(grid)):
		for y in range(len(grid[x])):
			if grid[x][y] == "1" and visitedGrid[x][y] == 'false':
				bfs(grid,visitedGrid,x,y)
				result += 1
	return result






'''grid = [["1","1","1","1","0"], ["1","1","0","1","0"], ["1","1","0","0","0"], ["0","0","0","0","0"]]'''
grid = [["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"]]
print(numIslands(grid))