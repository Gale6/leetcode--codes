def pacificAtlantic(heights):
	rbound, cbound = len(heights),len(heights[0])
	pac, atl = set(),set()


	def dfs(r,c,visit,preHeight):
		if ((r,c) in visit or r < 0 or c < 0 or r== rbound or c == cbound or heights[r][c] < preHeight):
			return
		visit.add((r,c))
		dfs(r + 1,c,visit,heights[r][c])
		dfs(r - 1,c,visit,heights[r][c])
		dfs(r,c + 1,visit,heights[r][c])
		dfs(r,c - 1,visit,heights[r][c])


	for c in range (cbound):
		dfs(0,c,pac,heights[0][c])
		dfs(rbound - 1, c, atl,heights[rbound-1][c])

	for r in range(rbound):
		dfs(r,0,pac,heights[r][0])
		dfs(r,cbound -1,atl,heights[r][cbound -1])

	res = []

	for s in pac:
		if s in atl:
			res.append(s)
	return res





heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

print(pacificAtlantic(heights))