#include <stdio.h>


int findMAxDiff (const int a[], int len) {

	int min[len];
	int max[len];

	if (len < 2) {
		printf("At least two expected");
		return -1;
	}

	int mini = 0;
	min[0] = 0;

	for (int i=0; i < len; i++) {
		if (a[i] < a[mini]) {
			mini = i;
		}
		min[i] = mini;
	}

	int maxi = len-1;
	max[maxi] = maxi;
	for (int i=len-2; i >= 0; i--) {
		if (a[i] > a[maxi]) {
			maxi = i;
		}
		max[i] = maxi;
	}

	int maxVal = 0;
	int x = -1;
	int y = -1;
	for (int i=0; i < len; i++) {
		int z = a[max[i]] - a[min[i]];
		if (z > maxVal) {
			maxVal = z;
			x = min[i];
			y = max[i];
		}
	}

	if (x == -1) {
		return -1;
	}
	return a[y] - a[x];

}

int main (int argc, char *args[]) {
	int a[] = {6,3};
	printf("MaxDiff = %d", findMAxDiff(a, 2));
}

