

def bioCoeff(n,k):
	n = n+1
	k = k+1
	bc = [ [0 for i in range(k)] for j in range(n)]

	for j in range(n):
		bc[j][0] = 1

	for i in range(1,n):
		for j in range(1,k):
			bc[i][j] = bc[i-1][j] + bc[i-1][j-1]

	print bc
	return bc[n-1][k-1]


print bioCoeff(5,3)				

