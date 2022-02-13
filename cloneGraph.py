def cloneGraph(node):
	hashOldToNew = {}

	def dfs(node):
		if node in hashOldToNew:
			return hashOldToNew[node]
		else:
			copy = Node(node.val)
			hashOldToNew[node] = copy
			for nei in node.neighbors:
				copy.neighbors.append(dfs(nei))
		return copy

	return dfs(node) if node else None