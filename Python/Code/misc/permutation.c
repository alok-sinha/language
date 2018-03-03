#include <stdio.h>


void swap (int A[], int i, int j){
	int tmp = A[i];

	A[i] = A[j];
	A[j] = tmp;
}

void printPermuation (int A[], int len) {
	printf("\n");
	for (int i=0; i <= len; i++) {
		printf("%d ", A[i]);
	}
}

void permutation (int A[], int len, int i, int *count) {

	if (i == len) {
		printPermuation(A, len);
		*count += 1;
		return;
	}

	for (int j = i; j <= len; j++) {
		swap(A,i,j);
		permutation(A, len, i+1, count);
		swap(A,i,j);
	}
}

int main (int argc, char *args[]) {
	int A[] = {1,2,3,4,5};
	int count = 0;
	permutation(A,4,0, &count);
	printf("\n Total count = %d", count);
}
