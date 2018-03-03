
#
# Programming pearls
# Chapter 2 : A file contains at most 4 billion 32 bit number. Find the missing one.
#             Since there are 0xffffffff(4,294,967,296) number possible, so 4,294,967,296 - 4,000,000,000 numbers must be missing
#
# ls -
# Solution 1 : With ample RAM available. 
#   use bit vector to represent each number. This requries 4,294,967,296/8 #bytes = 536,870,912 bytes of memory (about 1/2 Gig)
#
# Solution 2 : With few RAM available, using srcatch disk files.
#             lowCount = 0
#             hightCount = 0  
#             low = 0
#             high = maxint
#             while high > low:
#                 mid = (low + high)/2
#                 nums = high-low
#                 for num in nums:
#                     if num > mid:
#                         highCount += 1
#                     else:
#                         lowCount += 1
#                 if lowCount <  highCount:
#                     high = mid - 1
#                 else:
#                     low = mid + 1
# 
#
#

class missingNumberInfile:
	def get_first_bit_zero(num):
		num = ~num
		return num^(num-1)

	def bitVectorImpl(self, nums):
		# bucket = number/8
		# bit number -> number%8
		bitMap = {}
		for num in nums:
			bucket = num/32
			bitNum = num % 32

			if bucket not in bitMap:
				bitMap[bucket] = 1 << bitNum
			else:
				bitMap[bucket] = bitMap[bucket] | (1 << bitNum)	

		for bucket in bitMap:
			if bitMap[bucket] != 0xffffffff:
				missingNum = bucket*32 + get_first_bit_zero(bitMap[bucket])
				return missingNum

	def binarySearchImpl(self, nums):


				

