

def isSumPossible2(nums, sumTofind):
	n = len(nums)
	d = {num:[num] for num in nums}

	for num in nums:
		for key in d.keys():
			if key != num:
				t = []
				for s in d[key]:
					if s + num == sumTofind:
						print num, d, d[key], s
						return True
					else:
						t.append(s + num)
				d[key].extend(t)			
	print d
	return False				

def isSumPossibleBottomUp(nums, sumTofind):
	n = len(nums) + 1
	sumTofind += 1

	d = [[False for i in range(sumTofind)] for j in range(n)]

	for i,num in enumerate(nums):
		for j in range(1,sumTofind):
			if num == j:
				d[i][j] = True
			elif num < j:
				for k in range(0,i):
					d[i][j] = d[k][j -num]

	print d
	return d[n-1][sumTofind-1]					

def isSumPossible(nums, sumTofind,d):


	if sumTofind in nums:
		return True

	if tuple(nums) in d and  sumTofind in d[tuple(nums)]:
		return True
	
	for num in nums:
		if sumTofind > num and isSumPossible(nums-{num}, sumTofind-num, d):
			if tuple(nums) in d:
				d[tuple(nums)][sumTofind] = True
			else:
				d[tuple(nums)] = {sumTofind : True}	
			return True

	return False

d = {(a): {a:True} for a in (2,4,3,9,13,20)}

print isSumPossibleBottomUp([2,4,3,9,13,20], 16)			