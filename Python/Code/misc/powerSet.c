#include <stdio.h>

void printSet(int A[], int n) {

	printf("\n{");
	for (int i=0; i < n; i++) {
		if (A[i] != -1) {
			printf("%d, ", A[i]);
		}
	}
	printf("}");

}

void powerSet (int A[], int n, int i, int *count) {

	if (i == n) {
		printSet(A, n);
		*count += 1;
		return;
	}

	powerSet(A, n, i+1, count);

	int t = A[i];
	A[i] = -1;
	powerSet(A, n, i+1, count);
	A[i] = t;
}

int main (int argc, char *args[]) {
	int A[] = {1,2,3,4,5};
	int count=0;
	powerSet(A,5,0, &count);
	printf("\nCount = %d", count);
}