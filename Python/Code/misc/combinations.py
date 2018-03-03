

def getCombinations(nums, i, k, result, combs):
	
	if k == 0:
		result.append(list(combs))
		return

	for i in range(i, len(nums)-k +1):
		combs.append(nums[i])
		getCombinations(nums, i+1, k-1, result, combs)
		combs.remove(nums[i])


result = []
getCombinations([1,2,3,4,5], 0,3, result,[])	
print result