	

import random

class Dbl:
	class Node:
		def __init__(self, val):
			self.value = val
			self.next = None
			self.prev = None


	def __init__(self):
		self.head = None
		self.tail = None

	def findNode(self,val):
		node = self.head
		while node:
			if node.value == val:
				return node
			node = node.next

		return None	
					
	def addNode(self,val):
		node = self.Node(val)
		node.next = self.head

		if self.head:
			self.head.prev = node
		
		self.head = node	

		if self.tail == None:
			self.tail = node

	def delNodeVal(self,val):
		node = self.findNode(val)
		if node:
			nextNode = node.next
			prevNode = node.prev

			if nextNode:
				nextNode.prev = prevNode
			else:
				self.tail = prevNode


			if prevNode:
				prevNode.next = nextNode
			else:
				self.head = nextNode			

	def printList(self):
		node = self.head
		while node:
			print node.value,
			node = node.next


dl = Dbl()

l = range(5)
#random.shuffle(l)

[dl.addNode(i) for i in l]
dl.printList()
n =  dl.findNode(2)
print n
dl.delNodeVal(10)
dl.printList()


				




