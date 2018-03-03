#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct TreeNode_ {
	struct TreeNode_ *left;
	struct TreeNode_ *right;
	int key;
} TreeNode;

void inorderWalk (TreeNode *root) {
	if (!root) {
		return;
	}
	inorderWalk(root->left);
	printf("\n Key = %d", root->key);
	inorderWalk(root->right);
}

bool binarySearch (TreeNode *root, int key) {

	TreeNode *node = root;

	while (node) {
		if (node->key == key) {
			return true;
		}
		if (node->key > key) {
			node = node->left;
		} else {
			node = node->right;
		}
	}
	return false;
}

void insertInTree(TreeNode **root, TreeNode *nodeToInsert)
{
	TreeNode *node;
	if (*root == NULL) {
		*root = node;
		return;
	}

	node = *root;


	while (node) {
		if (node->key > nodeToInsert->key) {
			if (node->left) {
				node = node->left;
			} else {
				node->left = nodeToInsert;
				return;
			}
		} else {
			if (node->right) {
				node = node->right;
			} else {
				node->right = nodeToInsert;
				return;
			}
		}
	}

}

TreeNode *buildTree (int nums[], int len) 
{
	int i;
	TreeNode *root=NULL;

	printf("\n Buildiing tree...");
	fflush(stdout);
	for (i = 0; i < len; i++) {
		printf("\n Adding  tree...%d ", nums[i]);
		fflush(stdout);
		
		TreeNode *tNode = (TreeNode *)calloc(1,sizeof(TreeNode));
		if (!tNode) {
			return NULL;
		}
		memset(tNode, 0, sizeof(TreeNode));
		
		tNode->key = nums[i];
		insertInTree(&root, tNode);
	}

	printf("\n Done ading  tree...%d ");
	fflush(stdout);

	
	return root;
}

int main (int argc, char *args[]) {
	int a[8] = {4,1,5,6,12,2,19,10};
	
	printf("Size = %d %x", (int)sizeof(a),a);
	TreeNode *root = buildTree(a, 8);
	inorderWalk(root);
	printf (" %d ", binarySearch(root, 10));
	printf (" %d ", binarySearch(root, 11));
}


