
#
#
# n = number of weights/values
# maxValue(w) = MAX(maxValue(w-W[i]) + V[i] : for all W[i] in W)
# 
#  DAG : Each node is pointed to by n nodes at most - node(W) is pointed by node(W-W[i]), where W >= W[i]. The weight
# of link is the maxValue(W-W[i]) + V[i]
#     The problem reudces to finding longest path in DAG.
#
def maxValue(weights, values, maxWeight):
	maxValues = {0:0}

	for w in range(1,maxWeight+1):
		tmp = 0
		for i in range(0, len(weights)):
			if w >= weights[i]:
				if maxValues[w-weights[i]] + values[i] > tmp:
					tmp = maxValues[w-weights[i]] + values[i]

		maxValues[w] = tmp
	print "Max value is ", maxValues[maxWeight]		

#
# Since we don't know if sub problem has already used the given weight, we can not use above
# alogorithm. 
# Now we have to consider weights being used to achieve a given weight 
#
# Init condition:
# K(w,0) : 0    if w < W[0]
#        : V[0] if w >= W[0]
#
# K(0, W[j]) = 0 for all j = 0,...n-1
#
def maxValueNoRepeat(weights, values, maxWeight):
	K = {}
	n = len(weights) # Number of items
	K[0] = {}
	for item in range(0, n):
		K[0][item] = 0 
	
	for w in range(1,maxWeight + 1):
		K[w] = {}
		if w >= weights[0]:
			K[w][0] = values[0]
		else:
			K[w][0] = 0
	print K	
			
	for w in range(1, maxWeight+1):
		for i in range(1, n):
			if weights[i] <= w:
				K[w][i] = max(K[w][i-1],  K[w-weights[i]][i-1] + values[i])
			else:
				K[w][i] = K[w][i-1]
	printTable(K, n, maxWeight)			

def printTable(K, n, maxWeight):
	print K[maxWeight][n-1]	
	for w in range(0,maxWeight + 1):
		print "Weight = ", w,
		for i in range(0, n):
			print K[w][i],
		print " "			
		

fromCache = 0
calculate = 0
def knapSackRepeatMemo(weights, values, weight, itemIndex, K):
	global fromCache
	global calculate

	print "Called with ", weight, itemIndex
	if (K[weight][itemIndex] is not None):
		print "Return from cache ", K[weight][itemIndex]
		fromCache += 1
		return K[weight][itemIndex]

	calculate += 1
	maxSoFar = 0
	for i in range(itemIndex, 0,-1):
		print "Checking index ", i, weight
		
		if weights[i] <= weight:
			tmp = knapSackRepeatMemo(weights, values, weight-weights[i], i-1,K) + values[i]
			if  tmp > maxSoFar:
				maxSoFar = tmp

	K[weight][itemIndex] = maxSoFar			 
	print "Set in cache", K[weight][itemIndex]	

	return 	K[weight][itemIndex]		


K = {}
weights = [6,3,4,2]
values = [30,14,16,9]
maxWeight = 10
n = len(weights) # Number of items
K[0] = {}
for item in range(0, n):
	K[0][item] = 0 
	
for w in range(1,maxWeight + 1):
	K[w] = {}
	if w >= weights[0]:
		K[w][0] = values[0]
	else:
		K[w][0] = 0
	for i in range(1, n):
		K[w][i] = None	
print K	


print knapSackRepeatMemo(weights, values,maxWeight, 3, K)
printTable(K, n, maxWeight)	
print "From cache {0}, calculated {1}".format(fromCache, calculate)
#maxValueNoRepeat([6,3,4,2], [30,14,16,9],10)			



