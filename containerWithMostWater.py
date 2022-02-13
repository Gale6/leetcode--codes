def maxArea(height):
	L= 0
	R = len(height)-1
	result = 0

	while L < R:
		curr = (R-L) * min(height[L],height[R])
		print(L,R,curr)
		result = max(result,curr)
		if height[L] >= height[R]:
			R -=1
		else:
			L += 1
	return result

a = [1,8,6,2,5,4,8,3,7]
b = [1,1]
c=[2,3,4,5,18,17,6]




print (maxArea(c))
