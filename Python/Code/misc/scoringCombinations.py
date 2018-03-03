
def printCombinations(sequence, i):
	if i == 0 or i not in sequence:
		print "##"
		return

	for item in sequence[i]:
		if (item == i):
			print "------"
			return
		print item, ",",
		print printCombinations(sequence, item)


def scoringCombinations(scores, finalScore):

	combinations = []
	sequence = {}
	for i in range(0, finalScore+1):
		combinations.append(0)
	
	for i in range(0, finalScore+1):
		for score in scores:
			if score <= i:
				if combinations[i-score] + score == i:
					print "i = {0}, score = {1}, combinations[i-score] = {2}".format(i, score, combinations[i-score])
					combinations[i] =  combinations[i-score] + score
					if i in sequence:
						sequence[i].append(i-score)
					else:
						sequence[i] = [i-score]	

	print combinations
	print sequence


	printCombinations(sequence, finalScore)






scores = [2,3,4,7]	
scoringCombinations(scores, 15)
