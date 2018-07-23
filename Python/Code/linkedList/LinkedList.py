class LinkedList:
	class __Node:
		def __init__(self, item):
			self.item = item
			self.next = None
			self.prev = None

	def printDetails(self):
		print("List Type ", self.__type)

	def __init__(self, listType):
		if listType != 1 and listType != 2:
			#print("Invalid list type ", listType)
			raise ValueError("Invalid list type", listType)
			

		self.__head = None
		self.__type = listType
		

	def __AddSingly(self,item):
		tmp = self.__Node(item)
		tmp.next = self.__head
		self.__head = tmp	

	def __AddDouble(self,item):
		tmp = self.Node(item)
		
		tmp.next = self.head
		if self.__head:
			tmp.prev = self.__head.prev
		self.__head = tmp

	def Add(self, item):
		if self.__type == 1:
			self.__AddSingly(item)
		elif self.__type == 2:
			self.__AddDouble(item)	
		
	
	def find(self, item):
		node,found = self.__head, False
		while node:
			if node.item == item:
				found = True
				break
			node = node.next	

		return found		


	def deleteNode(self, node):
		pass

	def deleteItem(self, item):
		if self.__head == None:
			return
		
		prev = None
		node = self.__head
		while node:
			if node.item == item:
				if prev:
					prev.next = node.next
				else:
					self.__head = node.next
				return	
			prev = node
			node = node.next
	def print(self):
		node = self.__head
		while node:
			print (node.item)
			node = node.next			

l = LinkedList(1)
#print ("ListType", l.__type)
l.printDetails()

for i in range(1,10):
	l.Add(i)
l.deleteItem(1)
l.print()	






