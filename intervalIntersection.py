def intervalIntersection(firstList,secondList):
	result = []
	if len(firstList) <= 0 or len(secondList) <= 0:
		return result
	pointerA = 0
	pointerB = 0
	while pointerA < len(firstList) and pointerB < len(secondList):
		if firstList[pointerA][0] <= secondList[pointerB][1] and secondList[pointerB][0] <= firstList[pointerA][1]:
			print(firstList[pointerA][0],firstList[pointerA][1],secondList[pointerB][0],secondList[pointerB][1])
			result.append([max(firstList[pointerA][0], secondList[pointerB][0]),min(firstList[pointerA][1],secondList[pointerB][1])])
		if firstList[pointerA][1] <secondList[pointerB][1]:
			pointerA += 1
		elif firstList[pointerA][1] == secondList[pointerB][1]:
			pointerA += 1
			pointerB += 1
		else:
			pointerB += 1
	return result


a = [[1,3],[5,9]]
b = []

print(intervalIntersection(a,b))