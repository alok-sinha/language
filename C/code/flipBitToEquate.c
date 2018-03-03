#include <stdio.h>


int flipBit (int x, int y) {

	int z = x ^ y;

	int count = 0;
	while (z) {
		count += 1;
		z = z & (z-1);
	}
	return count;
}

int main (int argc, char *args[]) {
	printf("\nDiffs : %x %x %d", 29, 14, flipBit(29, 14));
}