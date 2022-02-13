def canJump(nums):
	if len(nums) == 1:
		return True
	canReach = nums[0]
	index = 0
	while canReach > index:
		index += 1
		canReach = max(canReach,index + nums[index])
		if index >= len(nums) - 1:
			return True
	return False
nums = [2,3,1,1,4]
print(canJump(nums))
