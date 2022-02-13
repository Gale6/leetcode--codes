def findCircleNum(isConnected):
	cities = []
	result = []
	currProvince = -1
	for i in range (len(isConnected)):
		cities.append(i)
	while len(cities) != 0:
		currProvince += 1
		result.append([])
		result[currProvince].append(cities.pop(0))

		currCheck = 0
		while currCheck < len(result[currProvince]):
			for j in range (len(isConnected)):
				if j not in result[currProvince]:
					if isConnected[result[currProvince][currCheck]] [j] == 1:
						result[currProvince].append(cities.pop(cities.index(j)))
			currCheck += 1
	return (len(result))


#isConnected = [[1,1,0],[1,1,0],[0,0,1]]

isConnected = [[1,0,0],[0,1,0],[0,0,1]]
print(findCircleNum(isConnected))