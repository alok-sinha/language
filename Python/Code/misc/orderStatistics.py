

def findKthSmallest(nums,k):
	n = len(nums)
	pi = random.sample(range(n))
	i = 0
	j = n-1

	while pi > i and pi < j:
		if nums[pi] < num[i]:
			while (nums[j] > nums[pi]) and j > pi:
				j = j-1
				if j > pi:
					swap(nums, i, j)
					i += 1
						j = j-1
						
