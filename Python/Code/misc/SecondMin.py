
import heapq

def secondMin(nums,k):

	h = []
	
	n = len(nums)
	start = 2
	if n%2 == 0:
		s1 = min(nums[0:2])
		s2 = max(nums[0:2])
		heapq.heappush(h, 0-nums[m])
		heapq.heappush(h, 0-nums[m])
	else:
		s1,s2 = nums[0], nums[0]
		start = 1

	for i in range(start, n-1, 2):
		if nums[i] < nums[i+1]:
			m = i
		else:
			m = i+1

		if len(h) < k:
			heapq.heappush(h, 0-nums[m])
		if nums[m] < s2:
			if nums[m] < s1:
				s2 = s1
				s1 = nums[m]
			else:
				s2 = nums[m]
		#print s1, s2		

	return s2


print secondMin([2, 8, 9, 4, 1, 10, 13, 20])							

			
