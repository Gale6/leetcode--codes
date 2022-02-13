def rob(nums):
    maxMoney = [None] * len(nums)
    maxMoney[0] = nums[0]
    if len(nums) > 1:
        maxMoney[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            maxMoney[i] = max((nums[i]+maxMoney[i-2]),maxMoney[i-1])
        return maxMoney[len(nums)-1]
    else:
        return maxMoney[0]

print(rob([1,2,3,1]))




def robWithoutLib(nums):
    r1 = 0
    r2 = 0

    for n in nums:
        newRob = max((n + r1),r2)
        r1 = r2
        r2 = newRob
    return r2
