#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct ListNode_ {
	struct ListNode_ *next;
	int val;
} ListNode_t;

const int nodeSize = sizeof(ListNode_t);


ListNode_t *reverseList (ListNode_t *head) {

	ListNode_t *prev = NULL;
	ListNode_t *node = head;

	while (node) {
		ListNode_t *tmp = node->next;
		node->next = prev;
		prev = node;
		node = tmp;
	}
	return prev;
}

void printList (ListNode_t *node){
	while (node) {
		printf("\n %d ", node->val);
		node = node->next;
	}
}

int insertNodeList (ListNode_t **head, int val) {
	ListNode_t *node = (ListNode_t *)malloc(nodeSize);
	if (!node) {
		return -1;
	}

	memset(node, 0, nodeSize);
	node->val = val;

	node->next = *head;
	*head = node;
	return 0;
}

ListNode_t *buildList(int nums[], int count) {

	int i;
	ListNode_t *head=NULL;

	for (i=0; i < count; i++) {
		insertNodeList(&head, nums[i]);
	}

	return head;
}

int main (int argc, char *args[]) {

	int ar [] = {1};
	ListNode_t *head = buildList(ar, 1);
	printList(head);
	head = reverseList(NULL);
	printList(head);
}



