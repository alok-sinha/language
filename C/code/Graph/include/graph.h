#ifndef __GRAPH_H__
#define __GRAPH_H__

typedef unsigned int node_t;
typedef int weight_t;

typedef struct GraphEdge_{
	node_t            peerNodeId;
	weight_t          weight;
	struct GraphEdge_ *next;
}GraphEdge_t;

typedef struct GraphNode_ {
	node_id     nodeId;
	GraphEdge_t *edges;
}GraphNode_t;

typedef GraphNode_t **Graph_t;


#endif

