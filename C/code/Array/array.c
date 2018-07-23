#include <stdio.h>

/*
 * Implement vector
 */


typedef struct {
	int capacity;
	void *items;
	int currentSize;
	int itemSize;
} vector;


vector *init_vector (int capacity, int sizeOfOneItem) {
	vector v = malloc(sizeof(vector));
	if (!v) {
		return NULL;
	}
	
	v->items = malloc(capacity*sizeOfOneItem);
	if (!v->items) {
		free(v);
		return NULL;
	}
	memset((char *)v->items, 0, capacity*sizeOfOneItem);
	v->capacity = capacity;
	v->currentSize = 0;
	v->itemSize = sizeOfOneItem; 

	return v;
}

int add_int_item (vector *v, int item) {
	if (v->capacity > v->currentSize) {
		v->items = relloac(v->items, 2*v->capacity);
		if (!v->items) {
			return -1;
		}
		/*
		 * Copy old to new array
		 */
		v->capacity = 2*v->capacity;
	}

	/*
	 * Capacity full, grow vector
	 */
	((int *)v->items)[v->currentSize] = item;
	v->currentSize++;
	return 0;
}


int main()
{
	vector *vec = init_vector(10, sizeof(int));
	if (!vec) {
		return 0;
	}
}