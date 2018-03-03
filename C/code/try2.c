
#include <stdio.h>
#include <stddef.h>

extern int i;
extern int c;

typedef struct {
	int a,b;
	double c,d;
} test_s;

test_s list[3];

struct abc {
	int a;
	int b;
};


void f (int n) {
	int a[n];

	a[1] = 1;
}

int
main ()
{ 
   abc a;
   int n=10;
   f(10);
   printf("%x %x", (size_t)list + 2*sizeof(test_s) + offsetof(test_s, c), &list);
}
