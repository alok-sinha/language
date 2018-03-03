
#Take care of heapify to use obly half array

numOfSwaps=0

def swap(nums, i, j):
	global numOfSwaps

	numOfSwaps += 1

	tmp = nums[i]
	nums[i] = nums[j]
	nums[j] = tmp

	

def bubbleUp(nums, lastIndex):
	child = lastIndex
	while child > 1:
		parent = child/2
		if nums[parent] < nums[child]: 
			swap(nums, child, parent)
		else:
			return
		child = parent		

def heapPop(nums, heapLength):
	num = nums[1]
	nums[1] = nums[heapLength]

	#Bubble down
	parent = 1
	while parent < heapLength:
		print "Parent = ", parent

		#Arbitrate between children, who is higher, if they exit	
		child1 = 2*parent
		higherChild = None
		if child1 <= heapLength:
			child2 = child1 + 1
			if child2 <= heapLength:
				if nums[child1] > nums[child2]:
					higherChild = child1
				else:
					higherChild = child2	
			else:
				higherChild = child1
			
		else:
			#We are done, no more child
			return num	

		if nums[parent] < nums[higherChild]:
			swap(nums,parent, higherChild)
			parent = higherChild	
		else:
			return num	

	return num			


def heapsort (nums):

	n = len(nums)
	#Heapify from left to right. We are creating max heap
	index = 2
	while index < n:
		bubbleUp(nums,index)
		print nums
		index += 1

	print nums

	#No pop from heap and store at end
	for i in range(1, n):
		num = heapPop(nums,n-i)
		print "Popped ", num, " new heap =", nums
		nums[n-i] = num

	print nums

#heapsort([0,4,6,1,2,9,20,15,13])
#heapsort([0,1,2,3,4,5,6,7,8])
heapsort([0,8,7,6,5,4,3,2,1])
print "Number of Swaps = ", numOfSwaps






