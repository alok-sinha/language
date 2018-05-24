#include <stdio.h>

void func (void) {
	int b[10]={};

	printf("\n%d", b[2]);
}

int main()
{
	int a[10];

	printf("\n%d", a[2]);
	func();
}