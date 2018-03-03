#maxsofar = 0 maxendinghere = 0 

#for i = [0, n) /* invariant: maxendinghere and maxsofar are accurate for x[ 0.. i-1] */ 
#  maxendinghere = max( maxendinghere + x[ i], 0) 
#  maxsofar = max( maxsofar, maxendinghere)

#
# maxendinghere is set to 0 if hits negative sum, which means we 
# re-start the sum. So next positive number will set it rolling again.
# So when we consider position i, we check maxendinghere so far for i-1, which 
# has started from a position where it was 0
#                 31, -41, 59, 26, -53, 58, 97, -93, -23, 84 
#MaxEndingHere :  31   0   59  85   32  90  187  84   61. 145
#MaxSofar         31   31  59  85   85  90  187  187  187 187  
#
 #x[i]    maxendinghere maxsofar
 # 31        31             31
 # -41       0              31
 # 59        59             59
 # 26        85             85
 # -53       32             85
 # 58.       90             90 
 # 97        187            187
 # -93       94             187
 # -23       71             187
 # 84        155            187 


#31, -41, 59, 26, -53, 58, 97, -93, -23, 84 

def max_sum(nums):
	n = len(nums)

	maxsofar = 0
	maxendinghere = 0
	begin = -1
	end = -1

	for i in nums:
		print "Checking ", i
		if (maxendinghere + i) < 0:
			maxendinghere = 0
			begin = -1
		else:
			maxendinghere = maxendinghere + i
			if begin == -1:
				begin = nums.index(i)

		if maxsofar  < maxendinghere:
		    maxsofar =  maxendinghere
		    end = nums.index(i)
		print "maxsofar = {0}, maxendinghere ={1}".format(maxsofar, maxendinghere)
	
	print "Begin = {0}, End = {1}, Max = {2}".format(begin, end, maxsofar)


#
# For finding sums from a given starting point, keep summing and upgrade to a # better one if found
#
def maxSumFromPosition(nums, startingIndex):
	maxsofar = 0
	sum = 0
	index = 0
	for i in range(startingIndex, len(nums)):
		sum += nums[i]
		if sum > maxsofar:
			maxsofar = sum
			index = i

	print "Maxsum starting from {0} = {1}, numners = {2}".format(startingIndex, maxsofar,nums[startingIndex : index+1])		


nums = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
maxSumFromPosition(nums, 5)
#max_sum(nums)

