def canJumpII(nums):
	result = 0
	l = r = 0

	while r < len(nums) - 1:
		furest = 0
		for i in range(l,r + 1):
			furest = max(furest, nums[i] + i)
		l = r + 1
		r = furest
		result += 1
	return result
