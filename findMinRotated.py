def findMin(nums):
	L = 0
	R = len(nums) -1
	while L<R:
		print(L,R)
		if nums[L]<nums[R]:
			return nums[L]
		mid = (L+R) // 2
		if nums[L] <= nums[mid]:
			L = mid + 1
		else:
			if nums[mid-1] > nums[mid]:
				return nums[mid]
			R = mid-1
	return nums[R]
print(findMin([4,5,1,2,3]))