

import heapq

class TreeNode:
	def __init__(self, count, left, right, c):
		self.count = count
		self.left = left
		self.right = right
		self.c = c	

	def getCount(self):
		return self.count	

	def visit(self,bit):
		self.bit = bit
		print "Count = {count}, Chars = {ch}".format(count=self.count, ch=self.c)
		if self.c != None:
			print "Code = ", bin(self.bit) 

		if self.left != None:
			self.left.visit(bit+"0")
		if self.right != None:
			self.right.visit(bit+"1")	



class HuffmanCode:

	def __init__(self, chars, freq):
		self.chars = chars
		self.freq = freq
		self.rootTree = None

	def prefixCodes(self):
		self.pqueue = []
		for c,f in self.freq.iteritems():			
			T = TreeNode(f, None, None, c)
			heapq.heappush(self.pqueue,(f,T))


		for i in range(0, len(self.chars)-1):
			t1 = heapq.heappop(self.pqueue)
			t2 = heapq.heappop(self.pqueue)

			if t1[0] > t2[0]:
				left = t2[1]
				right = t1[1]
			else:
				left = t1[1]
				right = t2[1]

			combinedNode = TreeNode(t1[0] + t2[0], left, right, None)
			self.rootTree = combinedNode

			heapq.heappush(self.pqueue, (t1[0] + t2[0], combinedNode))

	def traverse(self):
		self.rootTree.visit("0")
	
	def __str__(self):
		return str(self.rootTree.getCount())		


h = HuffmanCode(['a', 'b', 'c', 'd', 'e','f'],	{'a':45, 'b':13, 'c':12, 'd':16, 'e':9, 'f':5} )
h.prefixCodes()	
h.traverse()	


