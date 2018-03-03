#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
	int i;
	int t[];
} test_t;

void func (char *str) 
{
	printf ("%s", str);
}

void func2(int *a) {
	printf("\n From func : %d", *a);
}


void func3 (void *v) {
	int *a = (int *)v;
	printf("\n%d", *a);
}

typedef struct node_ {
	struct node_ *next;
	int val;
}node_t;

void func4 (int i, int j)
{
	
	int arr[i][j];

	arr[0][1] = 10;
	printf("%d", arr[0][0]);
}


void func5 (int m, int n, int a[n][m]) {
	int b[m];
}

int
main (int argc, char *args[]) {

	/* node_t **a;
	int k = 100;
	static int j = k;
	static test_t test={j*2};
	test.t[0] = 10;
	int *p;
	int x[10];

	printf("%d %d\n", sizeof(p), sizeof(x) );
	a = (node_t **)malloc(10*sizeof(node_t *));
	for (int i=0; i < 10; i++) {
		a[i] = (node_t *)malloc(sizeof(node_t));
		a[i]->val = i;
	}


	for (int i=0; i < 10; i++) {
		printf("%d %d", a[i]->val, test.i);
	}*/

	int a[2][3] = {{1,2,3}, {4,5,6}};
	printf("%x %x",a, **(a+1));
	func5(2,3, a);


	//func4(10,20);

}

