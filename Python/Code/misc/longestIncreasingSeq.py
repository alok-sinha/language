


def longestIncSeq(nums):
	d = {}
	n = len(nums)

	d[nums[0]] = [nums[0]]

	for i in range(1,n):
		maxForThisNum = 0
		maxIndex = 0
		for j in range(0,i):
			if nums[i] > nums[j]:
				if len(d[nums[j]]) > maxForThisNum:
					maxForThisNum = len(d[nums[j]])
					maxIndex = j


		d[nums[i]] = list(d[nums[maxIndex]])
		d[nums[i]].append(nums[i])

	t = map(len,d.values())
	print t.index(max(t))
	print max(map(len,d.values()))	

longestIncSeq([2,4,3,5,1,7,6,9,8])	
