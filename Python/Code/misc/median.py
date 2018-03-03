

class heap:
	def __init__(self, capacity):
		self.capacity = capacity
		self.heap = [0]*capacity


	def add(self,val):

	def getMin(self):

	def extractMin(self)	


class Median:
	def __init__(self,  nums):
		n = len(nums)

		if n == %2:
			k = n/2
			self.isOuter = True
		else:
			k = n/2+1
			self.isOuter = False	

		self.heap = heap(k)

		self.firstIndex = self.heap.add(nums[0])
		for i in range(1,k):
			self.heap.add(nums[i])

		
		self.outer = None
		for i in range(k, n):
			if self.outer:
				if nums[i] < self.outer:
					continue
				else:
					if nums[i] < self.heap.getMin():
						self.outer = nums[i]
					else:
						self.outer = self.h.extractMin()
						self.heap.add(nums[i])
			else:
				if nums[i] > self.getMin():
					self.outer = self.h.extractMin()
					self.heap.add(nums[i])	
				else:
					self.outer = nums[i]				

		if self.isOuter:
			self.median = (self.heap.getMin() + self.outer)/2
		else:
			self.median = self.heap.getMin()				


	def addNext(self, nextNum):
		self.h.delNodeFromIndex(self.firstIndex)
		
		if nextNum > self.outer:





		#return median	
