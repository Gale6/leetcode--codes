def searchMatrix(matrix,target):
	if len(matrix) == 0:
		return False
	up = 0
	down = len(matrix)-1
	while up<down:
		midV = (up+down+1) // 2
		if matrix[midV][0] == target:
			return True
		elif matrix[midV][0] > target:
			down =  midV - 1
		else:
			up = midV
	L = 0
	R = len(matrix[up]) - 1
	while L < R:
		midH = (L+R) // 2
		if matrix[up][midH] == target:
			return True
		elif matrix[up][midH] > target:
			R = midH - 1
		else:
			L = midH + 1
	if matrix[up][L] == target:
		return True
	else:
		return False



print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))