
class TrieNode:
	def __init__(self,c):
		self.char = c
		self.terminating = None
		self.childNodes = {}

def buildTri(words):

	def printNodeRecur(triNode):
		print triNode.char,
		if triNode.terminating:
			print "$"

		for c1, childTriNode in triNode.childNodes.iteritems():
			printNodeRecur(childTriNode)
			print " "

	def printTrie():
		for c,triNode in tri.iteritems():
			print "Trie starting with ", c
			printNodeRecur(triNode)

	
	tri = {}
	for word in words:
		if word[0] in tri:
			triNode = tri[word[0]]
		else:
			triNode = TrieNode(word[0])
			tri[word[0]] = triNode


		for c in word[1:]:
			if c in triNode.childNodes:
				triNode = triNode.childNodes[c]
			else:
				triNode.childNodes[c] = TrieNode(c)
				triNode = triNode.childNodes[c]

		triNode.terminating = True

	printTrie()
	return tri

def searchTrie(trie, word):

	triNode = None
	if word[0] in trie:
		triNode = trie[word[0]]
	else:
		print "Word not present"
		return False


	for c in word[1:]:
		if c in triNode.childNodes:
			triNode = triNode.childNodes[c]
		else:
			print "Word not present"
			return False

	return triNode.terminating		


t = buildTri(["ball", "balls", "bat", "buy", "busy"])
print searchTrie(t, "bald")					  


