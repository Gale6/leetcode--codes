def updateMatrix(mat):
	distanceMatrix = []
	queue = []
	for i in range(len(mat)):
		distanceMatrix.append([])
		for j in range(len(mat[i])):
			if mat[i][j] == 0:
				distanceMatrix[i].append(0)
				queue.append([i,j])
			else:
				distanceMatrix[i].append(float('inf'))
	#print ('distanceMatrix')
	#print to do list

	'''for dis in distanceMatrix:
		print(dis)'''	
	'''for q in queue:
		print(q)'''
	while len(queue) != 0:
		target = queue.pop(0)
		#print (target)
		tI = target[0]
		tJ = target[1]

		dirtMatrix = [[-1,0],[1,0],[0,-1],[0,1]]
		for d in dirtMatrix:
			newtI = tI + d[0]
			newtJ = tJ + d[1]
			#print('newtItJ',newtI,newtJ)

			if 0 <= newtI and newtI <len(mat) and 0<= newtJ and newtJ < len(mat[newtI]):
				#print('newtItJinIf',newtI,newtJ)
				if distanceMatrix[tI][tJ] + 1 < distanceMatrix[newtI][newtJ]:
					distanceMatrix[newtI][newtJ] = distanceMatrix[tI][tJ] + 1
					queue.append([newtI,newtJ])
	return distanceMatrix




a = [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]
result = (updateMatrix(a))

print('result')
for r in result:
	print(r)