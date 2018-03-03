

def findWinnerIndex(nums):

	
	n = len(nums)
	indexToCompare = range(n)

	while n > 1:
		winningIndex = []
		for i in range(0,len(indexToCompare),2):

			print i
			if i < (len(indexToCompare)-1):
				if nums[indexToCompare[i]] > nums[indexToCompare[i+1]]:
					winningIndex.append(indexToCompare[i])
				else:
					winningIndex.append(indexToCompare[i+1])
			else:
				winningIndex.append(indexToCompare[i])	
	
		n = n/2
		
		indexToCompare= list(winningIndex)
		print indexToCompare
	
	return winningIndex			

print findWinnerIndex([3,200,4,5,10,20,100,10,300])

				
