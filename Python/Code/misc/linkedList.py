


class ListNode:
	def __init__(self,value):
		self.value = value
		self.next = None



def addNodeList(head, value):

	if head == None:
		return(ListNode(value))

	node = ListNode(value)
	node.next = head
	head = node

	return head



def printList(head):
	node = head
	while node != None:
		print node.value
		node = node.next


head = None
for i in range(1,10):
	head = addNodeList(head, i)

printList(head)					