
#
# LCS(i,j) = 0, if i == 0, or j == 0
#          = 1 + LCS(i-1, j-1), if S1[i] == S2[j]
#          = max(LCS(i-1, j), LCS(i, j-1)), if S1[i] != S2[j]
#

def findLCSReversed(s1, s2):

	print "Strings : ", s1, ": ", s2
	LCS =  [[0 for i in xrange(len(s2)+1)] for i in xrange(len(s1)+1)]
	sequence =  [["0" for i in xrange(len(s2)+1)] for i in xrange(len(s1)+1)]

	for i in range(1, len(s1) +1):
		for j in range(len(s2), 0, -1):		
			if s1[i-1] == s2[j-1]:
				LCS[i][j] = 1 + LCS[i-1][j-1]
				sequence[i][j] = sequence[i-1][j-1] + s1[i-1]
			else:
				if LCS[i][j-1] > LCS[i-1][j]:
					LCS[i][j] = LCS[i][j-1]
					sequence[i][j] = sequence[i][j-1]
				else:
					LCS[i][j] = LCS[i-1][j]
					sequence[i][j] = sequence[i-1][j]
				
				

	print sequence[len(s1)][len(s2)], len(sequence[len(s1)][len(s2)])-1
	return LCS[len(s1)][len(s2)],sequence[len(s1)][len(s2)],

def reverseString(s):
	s1 = ""
	for i in range(len(s)-1, -1, -1):
		s1 = s1 + s[i]

	return s1	



def findLCS(s1, s2):
	print "Strings : ", s1, ": ", s2
	LCS =  [[0 for i in xrange(len(s2)+1)] for i in xrange(len(s1)+1)]
	sequence =  [["0" for i in xrange(len(s2)+1)] for i in xrange(len(s1)+1)]

	for i in range(1, len(s1) +1):
		for j in range(1, len(s2) +1):		
			if s1[i-1] == s2[j-1]:
				LCS[i][j] = 1 + LCS[i-1][j-1]
				sequence[i][j] = sequence[i-1][j-1] + s1[i-1]
			else:
				if LCS[i][j-1] > LCS[i-1][j]:
					LCS[i][j] = LCS[i][j-1]
					sequence[i][j] = sequence[i][j-1]
				else:
					LCS[i][j] = LCS[i-1][j]
					sequence[i][j] = sequence[i-1][j]
				
				

	print sequence[len(s1)][len(s2)], len(sequence[len(s1)][len(s2)])-1
	return LCS[len(s1)][len(s2)],sequence[len(s1)][len(s2)],


s1 = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"
s2 = "GTCGTTCGGAATGCCGTTGCTCTGTAAA"

#s1 = "abcde"
#s2 = "ae"

print findLCS(s1, s2)					

def longestPalindrom(s):
	maxSoFar = 0
	maxSubstring = ""
	for i in range(1,len(s)):
		s1 = s[:i]
		s2 = s[i-1:]

		length, subString = findLCSReversed(s1, s2)
		if length > maxSoFar:
			maxSubstring = subString
			maxSoFar = length

	print maxSoFar, maxSubstring

#longestPalindrom("character")			







