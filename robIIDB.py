def robII(nums):

	def robWithoutLib(nums):
	    r1 = 0
	    r2 = 0

	    for n in nums:
	        newRob = max((n + r1),r2)
	        r1 = r2
	        r2 = newRob
	    return r2
	return max(nums[0],robWithoutLib(nums[1:]),robWithoutLib(nums[:-1]))
nums = [1,3,1,3,100]
print(robII(nums))

