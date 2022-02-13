def search(nums,target):
	if len(nums) == 0:
		return -1
	L = 0
	R = len(nums)-1
	while L<R:
		mid = (L+R) // 2
		if nums[mid] == target:
			return mid

		if nums[L] < nums[mid]:
			if nums[L] <= target and target <=nums[mid]:
				if nums[L] == target:
					return L
				if nums[mid] == target:
					return mid
				R = mid - 1
			else:
				L = mid + 1
		else:
			if nums[mid+1] <= target and target <=nums[R]:
				if nums[mid+1] == target:
					return (mid+1)
				if nums[R] == target:
					return R
				L = mid + 2
			else:
				R = mid - 1
	if nums[L] == target:
		return L
	else:
		return -1



print(search([3,1],1))