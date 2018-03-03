

def decomposeStr(s):
	def isValid(word):
		return word in ["bed", "bath", "and", "beyond", "bat"]

	n = len(s)
	d = [[False for i in range(n)] for j in range(n)]

	for i in range(n):
		for j in range(i, n):
			if isValid(s[i:j]):
				d[i][j] = True

	for i in range(n-1):
		if d[0][i] and d[i+1][n-1]:
			return True

	print d
	return False

print decomposeStr("bedbathandbeyond")						

