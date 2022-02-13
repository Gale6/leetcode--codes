def rob(nums):
	maxMoney = [None] * (len(nums))
	maxMoney[len(nums) - 1] = nums[len(nums) - 1]
	def backtracking (nums,checking,maxMoney):
		if maxMoney[checking] != None:
			return maxMoney[checking]
		else:
			if checking + 2 < len(nums):
				robcheckingHouse = nums[checking] + backtracking(nums,checking+2,maxMoney)
			else:
				robcheckingHouse = nums[checking]
			notRobcheckingHouse = backtracking(nums,checking+1,maxMoney)
			maxMoney[checking] = max(robcheckingHouse,notRobcheckingHouse)
			return maxMoney[checking]
	return backtracking(nums,0,maxMoney)


print(rob([0]))