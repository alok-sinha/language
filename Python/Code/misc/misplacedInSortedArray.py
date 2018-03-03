

def misplacedNum(nums):
	
	if nums[0] > nums[1]:
		print "Misplaced ", nums[0]
		return

	misplacedNums = []
	for i in range(1, len(nums)-1):
		if nums[i-1] not in misplacedNums and ( (nums[i] > nums[i-1]) and (nums[i+1] < nums[i])):
			print "Misplaced ", nums[i]
			misplacedNums.append(nums[i])
		
		elif nums[i-1] not in misplacedNums and ((nums[i] < nums[i-1]) and (nums[i+1] > nums[i])): 	
			print "Misplaced ", nums[i]
			misplacedNums.append(nums[i])



misplacedNum([2,9,5,8, 3, 10,13])			

