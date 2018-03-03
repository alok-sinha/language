
from collections import *

class TreeNode:
	def __init__(self, key, left, right):
		self.key = key
		self.left = left
		self.right = right
		self.parent = None
	
	def setLeft(self, left):
		self.left = left

	def setRight(self, right):
		self.right = right	

	def setParent(self, parent):
		self.parent = parent	

def createMinimalTree(nums):
	if nums is None or len(nums) <= 0:
		return None

	if len(nums) == 1:
		return TreeNode(nums[0], None, None)	

	mid = len(nums)/2

	root = TreeNode(nums[mid], None, None)
	root.left = createMinimalTree(nums[:mid])
	root.right = createMinimalTree(nums[mid+1:])
	
	if root.left != None:
		root.left.parent = root
	
	if root.right != None:
		root.right.parent = root

	return root


def deleteNode(root, val):
	n  = binarySearch(root, val)
	if not n:
		return

	if n.right and n.left:
		succ = successor(n,val)
		print n
		print succ.parent
		n.key = succ.key

		deleteNode(n.right, succ.key)
	elif n.left != None:
		if n.parent.left == n:
			n.parent.left = n.left
		else:
			n.parent.right = n.left	

	elif n.right != None:
		if n.parent.right == n:
			n.parent.right = n.left
		else:
			n.parent.right = n.left	
	else:
		if n.parent.left == n:
			n.parent.left = None
		else:
			n.parent.right = None			






		

def createTree(nums):

	def insertNode(root, node):

		while root != None:
			if root.key > node.key:
				if root.left == None:
					root.left = node
					node.setParent(root)
					return
				else:
					root = root.left
						
			else:
				if root.right == None:
					root.right = node
					node.setParent(root)
					return
				else:
					root =  root.right							

	root = None
	for num in nums:
		node = TreeNode(num, None, None)
		if root == None:
			root = node
		else:	
			insertNode(root, node)

	return root


def checkBalanced(root):

	if root == None:
		return 0, True

	hLeft,isLeftBalanced = checkBalanced(root.left)
	hRight,isRightBalanced = checkBalanced(root.right)

	if isLeftBalanced == False or isRightBalanced == False:
		return 0, False

	if abs(hRight - hLeft) > 1:
		print "Unbalanced at ", root.key
		return 1 + max(hLeft, hRight),False
	else:
		return 1 + max(hLeft, hRight),True 



def printTreeLevels(root):
	d = deque()

	d.append(root)
	level = 1
	count = 1
	nextlevelcount = 0
	listOfNodes = []
	l = []
	while d:
		t = d.popleft()
		print t.key,
		l.append(t.key)	

		if t.left != None:
			d.append(t.left)
			nextlevelcount += 1
		
		if t.right != None:
			d.append(t.right)
			nextlevelcount += 1

		count -= 1
		if count == 0:
			count = nextlevelcount
			level += 1
			nextlevelcount = 0
			print " "
			listOfNodes.append(list(l))
			l = []

	print listOfNodes		
			


def TreeHeight(root):
	if root == None:
		return 0

	return 1 + max(TreeHeight(root.left),TreeHeight(root.right))	

def TreeMin(root):
	if root.left != None:
		return TreeMin(root.left)
	else:
		return root	

def TreeMax(root):
	if root.right != None:
		return TreeMax(root.right)
	else:
		return root.key	

def inorderWalk(root):
	if root == None:
		return

	inorderWalk(root.left)
	print root.key,
	inorderWalk(root.right)		


def binarySearchIter(root, key):

	while root != None:
		if root.key == key:
			return root
		elif key < root.key:
			root = root.left
		else:
			root = root.right	 	

	return None	

def binarySearch(root, key):
	if root == None:
		return None

	if root.key == key:
		return root

	if key < root.key:
		return (binarySearch(root.left, key))
	else:
		return (binarySearch(root.right, key))		

def successor(root, key):
	node = binarySearch(root, key)
	if node != None:
		if node.right != None:
			return TreeMin(node.right)

		parent = node.parent
		while (parent != None) and (parent.left != node):
			node = parent
			parent = parent.parent	

		return parent
	return None	

def predecssor(root, key):
	node = binarySearch(root, key)
	if node != None:
		if node.left != None:
			return TreeMax(node.left)

		parent = node.parent
		while (parent != None) and (parent.right != node):
			node = parent
			parent = parent.parent	

		return parent

def allThingsGreater(root, key):
	node = binarySearch(root, key)
	if node.right != None:
		inorderWalk(node.right)	

	parent = node.parent
	while parent != None:
		if parent.left == node:
			print parent.key,
			inorderWalk(parent.right)
		node = parent
		parent = parent.parent


root = createTree([15,6,18,3,7,17,20, 2,4,13,9])
#root1 = createMinimalTree([1,2,4,5,7,8,10,12,14,16])	
#print "Tree height = ", TreeHeight(root1)
#print checkBalanced(root)
#printTreeLevels(root)
inorderWalk(root)
printTreeLevels(root)
deleteNode(root,6)
printTreeLevels(root)

#print "\nMin", TreeMin(root1)
#print "Max", TreeMax(root)	

#print "Search ", binarySearchIter(root, 2)	
#print "Successor ", successor(root, 13).key
#print "predecssor ", predecssor(root, 9).key
#allThingsGreater(root, 6)





