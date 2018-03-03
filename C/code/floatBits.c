#include <stdio.h>
#include <math.h>

unsigned int binaryDouble (double a){

	unsigned int b = 0;

	double x = 0.5;
	for (int i=0; i < 32 && a; i++) {
		printf("\nx = %f", x);
		if (x <= a) {
			b = b | (1 << i);
			a = a - x;
		}
		x = x/2;
	}

	printf("\nFinal a = %f, b= %x", a, b);
	if (a == 0.0) {
		return b;
	} else {
		return -1;
	}

}

int 
main (int argc, char *args[]) {
	printf("\n%u", binaryDouble(0.75));
}
