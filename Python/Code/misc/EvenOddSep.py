

def evenOddSep(nums):
	def swap(nums, i,j):
		n
	def isEven(n):
		return n%2 == 0

	def isOdd(n):
		return n%2 != 0
			

	l = 0
	r = len(nums)-1

	while l < r:
		if isOdd(nums[l]):
			if isEven(nums[r]):
				nums[r], nums[l] = nums[l], nums[r]
				l = l +1 
			r = r-1		
		else:
			l += 1	


	print nums

print evenOddSep([2,5,7, 2,9,6])			

				 