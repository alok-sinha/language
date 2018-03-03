#include <stdio.h>

void func (int a[]) {
	printf("\n%d", sizeof(a)/sizeof(a[0]));
}

int main (int argc, char *args[]) {

	int a[]= {1,2,3,4,5,6};
	int b[6]= {[5]=10};
	int *p, *p2;

	p = p2*4;

	func(a);
	printf ("\n %d %d", sizeof(a), sizeof(p));


}