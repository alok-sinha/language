
#BFS works for both, directed and undirected graph
import heapq

class graphEdge:
	def __init__(self, weight, graphNode):
		self.weifght = weight
		self.graphNode = graphNode


class graphNode:
	def __init__(self, val):
		self.value = val
		self.adj = []
	
	def addAdj(self, graphNode, weight):
		self.adj.append(graphEdge(weight,graphNode))

	def getVal(self):
		return self.value

	def getAdj(self):
		return self.adj

	def printNode(self):
		print "----------------------------------"
		print "Value ", self.value, 
		print ",Adjacenncies"
		for node in self.adj:
			print "Value = ", node.getVal()		


nodes = {
	'r':['v','s'],
	's':['r', 'w'],
	'w':['s','t', 'x'],
	't':['w','x', 'u'],
	'x':['w', 't', 'u', 'y'],
	'u':['t', 'x', 'y'],
	'y':['x', 'u'],
	'v':['r']
}

nodes2 = {
	'y': ['x'],
	'x': ['z'],
	'z':['y','w'],
	'w' :['x'],
	's' : ['z','w'],
	'v' : ['s', 'w'],
	't' : ['v', 'u'],
	'u' : ['t', 'v']
}


class Graph:
	def __init__(self, nodes):
		self.graph = {}

		for node in nodes:
			gnode = graphNode(node)
			self.graph[node] = gnode

		for node in nodes:
			gnode  = self.graph[node]
			for adj in nodes[node]:
				if adj in self.graph:
					gnode.addAdj(self.graph[adj])
				else:
					print "Failed to find node {0} in graph ".format(adj)	

	def BFS(self,startNode, endNode):
		
		self.dia
		self.bfsQueue = [startNode]
		self.bfsInfo = {}
		for nodeId in self.graph:
			self.bfsInfo[nodeId] = {"color": "White", "Parent": None, "Distance": 0}
		
		self.bfsInfo[startNode]["Path"] = ""
		while len(self.bfsQueue) > 0:
			currentNode = self.bfsQueue.pop() # Next node id to visit
			currentGraphNode = self.graph[currentNode] #Graph node for this node id
			currentNodeBfsInfo = self.bfsInfo[currentNode] #BFS info for this node
			currentNodeBfsInfo["color"] = "Grey"
			
			print "Visited ", currentNode

			for adj in currentGraphNode.getAdj():
				adjId = adj.getVal()
				
				if endNode != None and endNode == adjId:
					return currentNodeBfsInfo["Distance"]+1, currentNodeBfsInfo["Path"]+currentNode + adjId

				
				adjNodeBfsInfo = self.bfsInfo[adjId]
				if adjNodeBfsInfo["color"] == "White":
					self.bfsQueue.insert(0, adj.getVal())
					adjNodeBfsInfo["color"] = "Grey"
					adjNodeBfsInfo["Parent"] = currentNode
					adjNodeBfsInfo["Distance"] = currentNodeBfsInfo["Distance"] +1 
					adjNodeBfsInfo["Path"] = currentNodeBfsInfo["Path"] +currentNode 

				currentNodeBfsInfo["color"] = "Black"	
		return self.bfsInfo		

	def printGraph(self):			
		for node in self.graph:
			self.graph[node].printNode()	

	def getPath(self, endNode, bfsInfo):
		
		path = [endNode]
		bfsInfoNode = bfsInfo[endNode]
		while bfsInfoNode["Parent"] != None:
			path.append(bfsInfoNode["Parent"])
			bfsInfoNode = bfsInfo[bfsInfoNode["Parent"]]
		return path, len(path)-1

	def someNodeUnexplored(self, dfsInfo, dfsStack):
		for node, nodeDfsInfo in dfsInfo.iteritems():
			if nodeDfsInfo["Color"] == "White":
				dfsStack.append(node)
				return True

		return False		

	def DFS(self, startNode):

		self.paranthesisHeap = []
		self.time = 0
		dfsInfo = {}
		for graphNode in self.graph: # Init dfs info for each node
			dfsInfo[graphNode] = {"Color":"White", "StartTime":0, 
			"FinishTime":0, "EdgeType":{}, "Adjacencies":[node.getVal() for node in self.graph[graphNode].getAdj()]}

		dfsStack = [startNode]
		while len(dfsStack) or Graph.someNodeUnexplored(self,dfsInfo, dfsStack): 
			print "Stack = ", dfsStack
			currentNode = dfsStack[-1] #Get top of stack
			currentNodeDfsInfo	= dfsInfo[currentNode]

			if currentNodeDfsInfo["Color"] == "White": #Color unexploted node and set time
				currentNodeDfsInfo["Color"] = "Gray"
				currentNodeDfsInfo["StartTime"] = self.time + 1
				self.time += 1 
				heapq.heappush(self.paranthesisHeap, (currentNodeDfsInfo["StartTime"], "(" + currentNode))
				print "Node {0}, startTime = {1}".format(currentNode, currentNodeDfsInfo["StartTime"])

			#Explore adjacancies of this node to see if there is any white node
			#If any Gray it, and put it on stack.
			#For non-white nodes, mark the edges to vertex as Back/Forward/Cross as the case may be.
			if currentNodeDfsInfo["Adjacencies"]:
				adjNodeId = currentNodeDfsInfo["Adjacencies"].pop()
				print "got adj as", adjNodeId
				adjNodeDfsInfo = dfsInfo[adjNodeId] 
				
				if adjNodeDfsInfo["Color"] == "White":
					dfsStack.append(adjNodeId)
					atLeastOne = True
					currentNodeDfsInfo["EdgeType"][adjNodeId] = "Tree"
				
				elif adjNodeDfsInfo["Color"] == "Gray":
					currentNodeDfsInfo["EdgeType"][adjNodeId] = "Back"

				elif adjNodeDfsInfo["Color"] == "Black":
					currentNodeDfsInfo["EdgeType"][adjNodeId] = "Cross/Forward"									
			else:
				dfsStack.pop()
				currentNodeDfsInfo["Color"] = "Black"
				currentNodeDfsInfo["FinishTime"] = self.time + 1
				heapq.heappush(self.paranthesisHeap, (currentNodeDfsInfo["FinishTime"],currentNode +")"))
				self.time += 1

		while self.paranthesisHeap:
			item = heapq.heappop(self.paranthesisHeap)
			print item[1],
		return dfsInfo	 		



class unionFind:
	def __init__(self, size):
		self.parent = range(size)
		self.treeSizes = [1 for i in range(size)]
		self.numberOfElements = size
	
	def find(self,node):
		while self.parent[node] != node:
			node = self.parent[node]

		return node

	def union(self, node1, node2):
		p1 = self.find(node1)
		p2 = self.find(node2)

		if self.treeSizes[p1] > self.treeSizes[p2]:
			self.parent[p2] = p1
			self.treeSizes[p1] += self.treeSizes[p2]
		else:
			self.parent[p1] = p2
			self.treeSizes[p2] += self.treeSizes[p1]

	def printUnion(self):
		for i,parent in enumerate(self.parent):
			print i, "->", parent, " -> ", self.treeSizes[i]					





g = Graph(nodes2)

#print g.BFS('v', None)
#print g.getPath('u', bfsInfo)

#g.printGraph()		

#g.printGraph()
#dfsG = g.DFS("s")
#print "Traversal",  dfsG
#for node, dfsInfo in dfsG.iteritems():
#	if dfsInfo["Color"] == "Black":
#		print "Explored node {0},  Start time = {1}, Finish Time = {2}, Edges = {3}".format(node, dfsInfo["StartTime"], dfsInfo["FinishTime"], dfsInfo["EdgeType"])

u = unionFind(4)
edges = [(0,3), (1,2),(2,3)]

for node1,node2 in edges:
	if u.find(node1) == u.find(node2):
		print "Graph has cycle "
		break
	else:
		u.union(node1, node2)





u = unionFind(6)
u.union(1,2)
u.union(2,4)
u.union(3,5)
u.printUnion()



