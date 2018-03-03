#include <stdio.h>
#include <stdlib.h>

typedef struct node_ {
	struct node_ *next;
	void *data;
	void *key;
}node_t;

typedef struct {
	node_t **table;
	int (*hashFunction)(void *item);
	bool (*keyCmpFunc)(void *key1, void *key2);
	int size;
} HashTable_t;


int intHashFunction (void *item) {
	int *key = (int *)item;


	return (*key)%61;
}

bool intKeyCmpFunction (void *key1, void *key2) {
	int *ikey1 = (int *)key1;
	int *ikey2 = (int *)key2;

	printf("\n Compare %d and %d", *ikey1, *ikey2);
	return *ikey1 == *ikey2;
}

int strHashFunction (void *item) {
	char *key = (char *)item;

	return 0;

}	

HashTable_t *init_hash_table(int size, int (*hashFunction)(void *item), bool (*keyCmpFunc)(void *key1, void *key2)) {

	HashTable_t *hashTable = (HashTable_t*)malloc(sizeof(HashTable_t));

	if (!hashTable) {
		return NULL;
	}

	hashTable->size = size;
	hashTable->table = (node_t **)malloc(size*sizeof(node_t *));
	if (!hashTable->table) {
		free(hashTable);
		return NULL;
	}

	hashTable->hashFunction = hashFunction;
	hashTable->keyCmpFunc  = keyCmpFunc;

	return hashTable;
}

int insert_hash_table (HashTable_t *hashTable, node_t *node) {
	int slot = hashTable->hashFunction(node->key);

	if (slot >= hashTable->size) {
		return -1;
	}

	printf("\n Insert in slot %d", slot);
	node_t *n = hashTable->table[slot];
	hashTable->table[slot] = node;
	node->next = n;

	return 0;
}

node_t *lookup_table (HashTable_t *hashTable, void *key) {
	int slot = hashTable->hashFunction(key);
	
	printf("\n Lookup in slot %d", slot);
	node_t *node = hashTable->table[slot];

	while (node) {
		if (hashTable->keyCmpFunc(node->key, key)) {
			return node;
		}
		node = node->next;
	}	

	return NULL;
	
}

void dumpTable (HashTable_t *ht) {

	for (int i=0; i < ht->size; i++) {
		node_t *node = ht->table[i];
		printf("\nSlot : %d", i);
		while (node) {
			printf(" %d ", *(int *)node->data);
			node = node->next;
		}

	}

}

int main (int argc, char *args[]) {
	HashTable_t *hashTable = init_hash_table(61, intHashFunction, intKeyCmpFunction);
	
	for (int i=0;i < 100; i++) {
		node_t *node = (node_t *)malloc(sizeof(node_t));
		
		int *value = (int *)malloc(sizeof(int));
		*value = i*i;
		int *key = (int *)malloc(sizeof(int));
		*key = i;

		node->data = (void *)value;
		node->key = (void *)key;
		insert_hash_table(hashTable, node);
	}
	dumpTable(hashTable);

	int key1 = 4;
	int key2 = 11;
	printf("\n %p %p ", lookup_table(hashTable, &key1),  lookup_table(hashTable, &key2));

}