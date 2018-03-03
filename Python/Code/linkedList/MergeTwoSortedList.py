
import random

class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None


def mergeSortedLists(l1, l2):

	def printList(l):
		while l:
			print l.val,
			l = l.next

	printList(l1)
	print " "
	printList(l2)

	if l1.val  > l2.val:
		head = l2
		higher = l1
		lower = l2
	else:
		head = l1
		higher = l2
		lower = l1

	while higher and lower:
		while lower.next and (lower.next.val < higher.val):
			lower = lower.next
		#print "lower {0}, higher {1}".format(lower.val, higher.val)
		x = lower.next	
		lower.next = higher
	
		tmp2 = higher
		higher = x
		lower = tmp2

	print "Return end"
	return head


r = [5,7,10,12]


r2 = [1,2,3,6,9,13]

head = None
head2 = None
for i in reversed(r):
	n = ListNode(i)
	n.next = head
	head = n

for i in reversed(r2):
	n = ListNode(i)
	n.next = head2
	head2 = n	

#while head:
#	print head.val,
#	head = head.next

#print ""	

				

print ""
head = mergeSortedLists(head, head2)
print "Done"

while head:
	print head.val,
	head = head.next	



