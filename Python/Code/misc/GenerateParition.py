


def generatePartition(n):
	print n
	
	if n == 1:
		return [[1]]

	part = []

	for i in range(1,n/2+1):
		p = generatePartition(n-i)
		print p,i

		for p1 in p:
			print "Appending", i, p1
			p1.append(i)
			part.append(p1)
			print part

	print "Return", part
	return part	

	





print generatePartition(5)


