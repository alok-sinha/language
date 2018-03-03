
from collections import deque

def minSqSum(n, nums, bfs):
	def getNgbs(x):
		y = []
		for num in nums:
			if (x - num) >= 0:
				y.append(x-num)
		return y

	
	q = deque()
	q.appendleft(n)

	while q:
		node = q.pop()
		
		ngbs = getNgbs(node)
		if 0 in ngbs:
			bfs[0] = node
			return True

		for ng in ngbs:
			if ng not in q:
				bfs[ng] = node
				q.appendleft(ng)

	return False				

bfs = {12:-1}
t =  minSqSum(12, [1,4,9], bfs)

if t == True:
	p  = bfs[0]
	s = 0
	while p != -1:
		print p-s
		s = p
		p = bfs[p]


