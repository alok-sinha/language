




def optimalStringCut(length, cuts, cache):
	
	if length in cache:
		cutsCost = cache[length]
		if cuts in cutsCost:
			print "Returning from cache	"
			return cutsCost[cuts] 

	print length, ":", cuts
	if len(cuts) == 1:
		return length
	elif len(cuts) == 0:
		return 0	

		

	minCost = 1000
	for i in range(0, len(cuts)):
		cutIndex = cuts[i]
		leftPortionLength = cutIndex
		rightPortion = length - leftPortionLength

		leftCuts = cuts[:i]
		rightCuts = tuple([(x - i) for x in cuts[i+1:]])
		cost = length + optimalStringCut(leftPortionLength, leftCuts, cache) +  optimalStringCut(rightPortion, rightCuts, cache)
		if cost < minCost:
			print "new cost ", cost, length
			minCost = cost

		if length in cache:
			cache[length][cuts] = cost
		else:
			print cuts
			cache[length] = {cuts:cost}	


	return minCost		
		

print optimalStringCut(20, (2,8,10), {})		
