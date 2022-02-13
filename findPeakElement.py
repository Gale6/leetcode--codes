def findPeakElement(nums):
	L=0
	R=len(nums)-1
	while L<R:
		mid = (L+R+1) // 2
		if nums[mid-1]>nums[mid]:
			R = mid -1
		else:
			L = mid
	return L
