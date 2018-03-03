



def maxCutRod(prices,n):

	r = {0:0}
	cuts = {0:0}

	for i in range(1,n+1):
		maxsofar = prices[i]
		optimalCut = i
		for j in range(1,i):
			if (prices[j] + r[i-j]) > maxsofar:
				maxsofar = prices[j] + r[i-j]
				optimalCut = j
		r[i] = maxsofar
		cuts[i] = optimalCut
	
	print r
	print cuts
	print r[n]

	while n > 0:
		print cuts[n],
		if n == cuts[n]:
			break
		else:
			n = cuts[n]	

				


maxCutRod([0,1,5,8,9,10,17,17,20, 24, 30], 7)	




