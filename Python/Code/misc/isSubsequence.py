
#
# This routine finds if s2 is subseqnece of s1. 
# Order of len(s1)
def isSubsSequence(s1, s2):

	if len(s1) == 0 or len(s2) == 0:
		return False

	i = 0
	for  j in range(0, len(s1)):
		if s1[j] == s2[i]:
			i += 1
			if i == len(s2):
				return True

	return False
					

print isSubsSequence("Alok", "")					