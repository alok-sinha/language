

import math

def countRightSetBits(n):
	x = ~n
	y = x ^ (x-1)
	print math.log(y+1,2)-1

def addBinaryNumbers(n1,n2):
	result = 0
	while n2:
		result = n1 ^ n2 
		carry = (n1 & n2) << 1 #Add carry to result
		n1,n2 = result, carry #continue adding carry if there is still any
	return result	


def multiplyNumbers(n1,n2):
	result = 0
	if n1 == 0 or n2 == 0:
		return 0

	shift = 0
	while n1:
		if n1 & 0x1:
			result += (n2 << shift)
		shift += 1
		n1 = n1 >> 1 

	return result	


def swapBits(x, size):
	print "Swapping ", bin(x), " size ", size
	if size == 2:
		return (x >> 1 | x << 1)
	return (swapBits(x & 0xffffffff, size/2) << size/2) | (swapBits((x >> size/2) & 0xffffffff, size/2))


#print addBinaryNumbers(10, 20)

#print bin((swapBits(0xabcdabcdabcdabcd, 64))), bin(0xabcdabcdabcdabcd)
countRightSetBits(11)
