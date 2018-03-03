
import graph
import heapq

def dijkstra(g, source):
	distance = {}
	notExplored = g.vertex()
	for vertex in notExplored:
		distance[vertex] = 0xff

	h = [source]
	while notExplored:
		v = heapq.heappop(h)
		explored.append(v)

		for nei in v.getAdj():
			if nei  in notExplored:
				if distance[nei]  > distance[v] + g.edgeWeight(v,nei):
					distance[nei] = distance[v] + g.edgeWeight(v,nei)
					notExplored.remove(nei)
					heapq.heappush(h, nei)
					


def prim(graph):
	mst = []
	vertices = graph.getVertices()
	edges = graph.getVertices()


	mst.append(vertices[0])
	vertices.remove(vertices[0])
	while vertices:
		winningEgde = min([getLowestNonMStEdge(v) for v in mst])
		otherVertex = winningEgde.getOtherVertex(winningEgde)
		mst.append(winningEgde)
		vertices.remove(otherVertex)

	return mst	

