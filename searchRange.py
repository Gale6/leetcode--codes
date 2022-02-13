def searchRange(nums,target):
	if len(nums) == 0:
		return [-1,-1]
	def searchFirst(nums,target):
		L = 0
		R = len(nums)-1
		while L<R:
			mid = (L+R) // 2
			if nums[mid] < target:
				L = mid+1
			elif nums[mid] == target:
				R = mid
			else:
				R = mid - 1
		if nums[L] != target:
			return -1
		return L
	def searchLast(nums,target):
		L = 0
		R = len(nums)-1
		while L<R:
			mid = (L+R+1) // 2
			if nums[mid] < target:
				L = mid+1
			elif nums[mid] == target:
				L = mid
			else:
				R = mid - 1
		if nums[L] != target:
			return -1
		return L
	return [searchFirst(nums,target),searchLast(nums,target)]

print(searchRange([5,7,7,8,8,10],8))