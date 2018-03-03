#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void init_out (int *out, int n) {
	for (int i =0; i < n; i++) {
		out[i] = 1;
	}
}

int *productExceptSelf (int A[], int n) {

	int *out = (int *)malloc(sizeof(int)*n);
	init_out(out,n);

	int m = 1;
	for (int i=0; i < n-1 ; i++) {
		m *= A[i];
		out[i+1] = m;
	}

	m = A[n-1];
	for (int i=n-2; i >=0 ; i--) {
		out[i] *= m;
		m *= A[i];
	}
	return out;
}


int main (int argc, char *args[]) {
	int A[] = {1,2,3,4,5};
	int *out = productExceptSelf(A, 5);

	for (int i=0; i < 5; i++) {
		printf("%d ", out[i]);
	}

}