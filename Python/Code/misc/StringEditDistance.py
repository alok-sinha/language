
#def perform_edit(s1, e, i, j):
#	t = e[i][j]
#	if t[1].find("Add") != -1:



def print_sequnce(e, i, j):
	t =  e[i][j]
	print t[1]
	if t[2] > 0 and t[3] > 0:
		print_sequnce(e, t[2], t[3])

#
# e(i,j) = e(i-1, j-1) if s1[i] == s2[j]
#        = 1 + min(e(i-1, j), e(i, j-1))
# 
#
# Initialiation : From substring to empty string
#                 e(0, i) = i
#                 e(i,0) = i 
#
# 1) How to handle different weighted operations?
# 2) How to track operations?
#
def editDistance(s1, s2):
	e = []
	for i in range(0, len(s1)+1):
		e.append([])
		for j in range(0, len(s2)+1):
			e[i].append((0,""))
	#e = [ [0]*len(s2) for i in s1]
	print e
	for i in range(1, len(s2) + 1):
		e[0][i] = (i,"")
	for i in range(1, len(s1) + 1):
		e[i][0] = (i, "")

	print e		


	for i in range(1, len(s1)+1):
		for j in range(1, len(s2)+1):
			s = "Matching char " + s1[i-1]  + " and " + s2[j-1]
			if s1[i-1]  != s2[j-1]:
				minVal = 0
				prev_i = 0
				prev_j = 0
				if e[i-1][j][0] < e[i][j-1][0]:
					if e[i-1][j][0] < e[i-1][j-1][0]:
						minVal = e[i-1][j][0]
						s = "Delet " + s1[i-1]
						prev_i = i-1
						prev_j = j
					else:
						minVal = e[i-1][j-1][0]
						s = "Sub {0} by {1}".format(s1[i-1], s2[j-1])
						prev_i = i-1
						prev_j = j-1
				else:
					if e[i][j-1][0] < e[i-1][j-1][0]:
						minVal = e[i][j-1][0]
						s = "Add " + s2[j-1]
						prev_i = i
						prev_j = j-1
					else:
						minVal = e[i-1][j-1][0]
						prev_i = i-1
						prev_j = j-1
						s = "Sub {0} by {1}".format(s1[i-1], s2[j-1])					


				e[i][j] = (1 + minVal, s, prev_i, prev_j)
			else:
				e[i][j] = (e[i-1][j-1][0], s, i-1, j-1)
	
	for i in range(0,len(s1)+1):
		for j in range(0, len(s2)+1):
			print e[i][j][0],
		print " "	

	return e, len(s1), len(s2)

#print editDistance("Carthorse", "Orchestra")
r,i,j = editDistance("Saturday", "Sundays")
#r,i,j = editDistance("S", "D")				 
#print editDistance("Carthorse", "Carthorse")         
print_sequnce(r,i,j)
#





