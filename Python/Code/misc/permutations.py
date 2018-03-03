


def getPermutations(nums):
	def fillPermutation(index,permutation, usedNums, nums):
		if index >= (len(nums)-1):
			print "permutation = ", permutation
			return 1

		count = 0
		for i in range(len(nums)):
			if usedNums[i] == False:
				usedNums[i] = True
				permutation[index] = nums[i]
				if index == (len(nums)-1):
					print "permutation = ", permutation
					count += 1
				else:
					c = fillPermutation(index+1, permutation, usedNums, nums)
					count += c	

				usedNums[i] = False		
		return count
				

	count = 0
	usedNums = [False for num in nums]
	for i in range(len(nums)):
		permutation = [0 for num in nums]
		
		permutation[0] = nums[i]
		usedNums[i] = True
		count += fillPermutation(1,permutation, usedNums, nums)
		usedNums[i] = False

	return count	

def nextPermutation(p):
	c = None
	for i in range(len(p)-1, 0, -1):
		if p[i-1] < p[i]:
			c = i-1
			break

	if c == None:
		print "No next permutation"
		return None

	c2 = min(filter(lambda x : x > p[c], p[c+1:]))
	i = p.index(c2)
	p[i] = p[c]
	p[c] = c2
	t = p[c+1:]
	t.reverse()
	#print p, c, t

	print "next permutation", p[:c+1] + t
	return p

p = [1,2,3,4,5]
count = 0
while p != None:
	p =  nextPermutation(p)
	count += 1

print "Total permutations", count	


#count = getPermutations([1,2,3,4,5])
#print "Total count ", count