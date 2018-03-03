
from  bisect import *


def findMedian(l1,l2,k):
	n1 = len(l1)
	n2 = len(l2)

	f,s,mi = (l1,l2, n1/2) if n1 > n2 else (l2,l2, n2/2)

	i = bisect(s, f[mi])
	k = k-mi
	
	if i == k:
		return s[i]
	else:
			




a = [2,4,5,7,10,12,13,18]
b = [9,11,14,16,20]

findMedian(a,b)

print bisect_left(a,1)
print bisect_right(a,1)
print bisect_left(a,4)
print bisect_left(a,2)
print bisect_left(a,13)
print bisect_left(a,14)
print bisect_right(a,14)
