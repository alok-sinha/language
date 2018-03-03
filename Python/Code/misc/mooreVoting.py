

def findMajority(nums):
	majIndex = 0
	majE = nums[0]
	count = 1
	for i in range(1, len(nums)-1):
		if nums[i] == majE:
			count += 1
		else:
			count -= 1
		if count == 0:
			majE = nums[i]
			count = 1

	if count > 0:
		return majIndex
	else:
		return -1	


print findMajority([3,2,3])			

						
