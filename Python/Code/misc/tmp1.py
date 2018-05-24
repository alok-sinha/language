
x = 1000

def findAllString(l, i, j):
	
	global x
	x = x*2
	print(x)
	found = False
	for k in range(i,j+1):
		if l[k] == '?':
			found = True
			break

	if found == False and k == j:
		print (l)
		return

	for m in (0,1):
		l[k] = m
		findAllString(l, i+1, j)
		l[k] = '?'


		
l = ['1','?','1','1','?','?']
findAllString(l, 0, len(l)-1)
print(x)
	