

def can3Sum(nums, cache, k, ls):

	def can2Sum(nums,s, i, cache):
		if s in cache:
			if i in cache[s]:
				return cache[s]

		i = 0
		j = len(nums)-1
		while i < j:
			x = nums[i] + nums[j]
			if  x == s:
				if s in cache:
					cache[s][i] = (True,nums[i], nums[j])
				else:
					cache[s] = {i: (True,nums[i], nums[j])}	

				return True, nums[i], nums[j]
			elif x > s:
				j -= 1
			else:
				i += 1	
		
		if s in cache:
			cache[s][i] = (False,  None, None)
		else:
			cache[s] = {i:(False,  None, None)}			
		return False,None,None					





	n = len(nums)
	if n == 3:
		return sum(nums) == 0
	
	if n <= 2:
		return False	

	r,num1, num2 = can2Sum(nums[1:],-nums[0], i+1, cache)
	if r == True:
		ls.append([nums[1:], num1, num2])
		return True

	return can3Sum(nums[1:], cache, ls)	


nums =  [-1, 0, 1, 2, -1, -4]
#nums = [-1,0,2,3,-4]
nums.sort()
cache = {}
ls = []
print can3Sum(nums, cache, ,0, ls)
print ls	