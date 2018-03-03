

class TrieNode:
	def __init__(self,suffix, children):
		self.chars = suffix
		self.children = children

	def addChild(self,suffix):
		
		n = len(suffix)
		newChars = self.chars[n:]
		self.chars = self.chars[:n]
		

		newNode = TrieNode(newChars, self.children)
		self.children = {newChars[0]:newNode} 	

	def findSbtring(self, strToSearch):
		def compare(le):
			for i in range(le):
				if self.chars[i] != strToSearch[i]:
					return False
			return True	
		
		l1= len(strToSearch)
		l2 = len(self.chars)

		if l1 <= l2:
			r = compare(l1)
			if r == False:
				return False

			return True		
		else:
			r = compare(l2)
			if r == False:
				return False

			rest = strToSearch[l1-1:]
			if rest[0] not in self.children:
				return False
			else:
				return self.children[rest[0]].findSbtring(rest)			 


				




trieRoot = {}
s = "abcdabc"
for i in range(0, len(s)):
	suffix = s[i:]
	if suffix[0] not in trieRoot:
		trieRoot[s[i]] = TrieNode(list(suffix), {})
	else:
		trieRoot[s[i]].addChild(suffix)		
	

def printTrieNode(node):
	print "Content ", node.chars,
	for child in node.children:
		print child,
		printTrieNode(node.children[child])


for c in trieRoot:
	print "\nTree under ", c
	printTrieNode(trieRoot[c])

print trieRoot['a'].findSbtring("abcd")	



