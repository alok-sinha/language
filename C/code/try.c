#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>



int  i = 0;
int c = 'a';

int *p1 = &i;
int *p2 = &c;

typedef struct s_t {
	int a;
	const char *s;
}s_t;

void func (int a[]) {
	//a[0]= 10;
}

int main (int argc, char *args[])
{
	static _Thread_local int k;

	char a[]= {'a','b', 'c','d'};
	printf("%d, %d", sizeof(a), strlen(a));
	char s[] = "alok";
	printf("\n%d",sizeof(s));
	const int b[] = {1,2,3};
	func((int *)b);

}