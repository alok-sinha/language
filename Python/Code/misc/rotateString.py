#
# 
# Chapter 2 : Roatate a string i place
#
# Reversal Approach
# ===================
#Rotate a string i places to right
# key idea : reverse first i char and rest n-i chars individually and then reverse the whole reverse string
# s = ab, where a is what needs to be rotated
#
# s(rotate) = reversed(reversed(a)reversed(b))
#
# Juggling approach
# =================
# 
# Assumuing a < b
# ab -> ab(l)b(r), where a and b(r) are of same length
#  Swap a and b(r) -> b(r)b(l)a
#  Now Swap b(r) and b(l) -> b(l)b(r)a
#

def reverse(l):
	n = len(l)
	for i in range(0, n/2):
		tmp = l[i]
		l[i] = l[n-i-1]
		l[n-i-1] = tmp
	
	return l
		

def rotateByReversing(string, i):
	n = len(string)
	s1 = reverse(string[0:i])
	s2 = reverse(string[i:])

	s3 = s1 + s2
	print reverse(s3)

def rotateByJuggling(string,i):
	if i >= string/2
		swap(string[:i], string[len(string)-i:])
		swap(string[i:len(string)-i], string[len(string)-i:])
	else:
		swap()	



rotateByReversing(list("abcdefghi"), 8)
rotate([], 2)	