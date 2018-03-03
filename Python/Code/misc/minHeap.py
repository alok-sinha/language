

import heapq

class maxHeap:
	def __init__(self):
		self.heap = []

	def push(self, item):
		heapq.heappush(self.heap,(0-item))
	
	def pop(self):
		return (0-heapq.heappop(self.heap))



h = maxHeap()


h.push(1)
h.push(0)
h.push(-1)
h.push(-2)
h.push(2)

	

h = []

l = range(-2,3)

for i in l:
	heapq.heappush(h, 0-i)	

for i in range(5):
	print 0-heapq.heappop(h)	




