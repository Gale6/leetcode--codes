def canFinish(numCourses,prerequisites):
	preMap = {i:[] for i in range(numCourses)}
	for prere in prerequisites:
		target, pre = prere
		preMap[target].append(pre)

	visited = set()
	def dfs(crs):
		if crs in visitedSet:
			return False
		if preMap[crs] == []:
			return True
		for pre in preMap[crs]:
			if not dfs(pre): return False
		visited.remove(crs)
		preMap[crs] = []
		return True
	for crs in range(numCourses):
		if not dfs(crs): return False
	return True