

def permutate(s, p):

	index = 0
	start = 0
	for i in range(len(p)):
		print s, index
		if start != p[index]:
			s[index], s[p[index]] = s[p[index]], s[index]
			prevIndex = index
			index = p[index]
			p[prevIndex] = -1
		else:
			for t,p in enumerate(p):
				if p != -1:
					start = t
					index = t
					break

	print s

permutate([1,2,3,4,5,6], [2,3,1,4,0,5])		

