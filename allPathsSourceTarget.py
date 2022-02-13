def allPathsSourceTarget(graph):
	target = len(graph) - 1
	result = []
	def dfs(curr,target,graph,path):
		
		if curr == target:
			path.append(curr)
			result.append(path)
		else:
			for i in graph[curr]:
				dfs(i,target,graph,path + [curr])
	dfs(0,target,graph,[])

	return result

graph = [[1,2],[3],[3],[]]

print(allPathsSourceTarget(graph))
