#include <stdio.h>

void updateMax (int count, int *maxCount) {
	if (*maxCount < count) {
		*maxCount = count;
	}
}

int max1SeqLen (int x) {


	int rCount = 0;
	int lCount = 0;
	bool left = false;

	int maxVal = 0;
	int i=0;

	while (i < 32) {
		char b = x & (1 << i);

		if (b) {
			if (left) {
				lCount += 1;
			} else {
				rCount += 1;
			}
		} else {
			if (!left) {
				left = true;
			}
			{
				printf("\ni : %d, l : %d, r : %d", i, lCount, rCount);
				updateMax(rCount + lCount + 1, &maxVal);
				left = false;
				rCount = lCount;
				lCount = 0;
			}
		}

		i  += 1;
	}
	updateMax(rCount + lCount + 1, &maxVal);
	return maxVal;
}

int main (int argc, char *args[]) {
	printf("\n Max seq len = %d", max1SeqLen(61308));

}

