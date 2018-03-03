#include <stdio.h>

void reverseBit(int i) {

	unsigned char maskl=0x01;
	unsigned char maskh=0x80;
	printf("Number before reversal %d", i);
	for (int j =0; j < 4; j++) {
		int x = i & maskl;
		int y = i & maskh;

		if (x != y) {
			i ^= maskl;
			i ^= maskh;
		}
		maskh = maskh >> 1;
		maskl = maskl << 1;
	}
	printf("New number = %d", i);

}

void f(int *a) {
	a = NULL;
}

int main (int argc, char *args[]) {
	reverseBit(20);
	int a[] = {1,2,4};
	//a = NULL:
	f(a);
}