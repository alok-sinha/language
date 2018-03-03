

def sort(nums):

	i = 0
	n = len(nums)
	count = 0
	while count < n:
		if nums[i] != (i+1):
			nums[nums[i]-1], nums[i]   = nums[i], nums[nums[i]-1]
		else:
			i += 1	
		
		count += 1	

	print nums


sort([6,5,4,3,2,1])		