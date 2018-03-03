

def mergeTwoSortedArrays(a, b):
	ai,bi = 0,0

	print "Merging. ", a, b
	c = []
	while ai < len(a) and bi < len(b):
		if a[ai] < b[bi]:
			c.append(a[ai])
			ai += 1
		else:
			c.append(b[bi])	
			bi += 1

	if (ai == len(a)):
		c.extend(b[bi:])

	elif bi == len(b):
		c.extend(a[ai:])

	print c	
	return c			




mergeTwoSortedArrays([1,3,5],[2,4,7,8])


def mergesort(nums):

	n = len(nums)
	if n <=1:
		return nums

	l1 = mergesort(nums[0:n/2])
	l2 = mergesort(nums[n/2:])


	return(mergeTwoSortedArrays(l1,l2))

def iterativeMergesort(nums):
	Q = [[num] for num in nums]
	print Q

	while len(Q) > 1:
		i1= Q.pop()
		i2= Q.pop()	
		Q.insert(0,mergeTwoSortedArrays(i1, i2))

	return Q.pop()	
	



#l = mergesort([5,1,7,8,4,2,10,20,15,18])
#print l
#print mergesort([1,2,3])
l = iterativeMergesort([5,1,7,8,4,2,10,20,15,18])	
print "Iter - ", l




