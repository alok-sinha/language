#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int min (int v1, int v2, int v3) {
	int w1  =  v1 < v2 ? v1 : v2;
	int w2  =  w1 < v3 ? w1 : v3;

	return w2;
}

int editDistance (const char *s1, const char *s2) {

	int l1 = strlen(s1) + 1;
	int l2 = strlen(s2) + 1;

	int edit[l1][l2];
	memset(edit, 0, sizeof(int)*l1*l2);
	for (int i=1; i < l1; i++) {
		edit[i][0] = 1;
	}
	for (int i=1; i < l2; i++) {
		edit[0][i] = 1;
	}

	for (int i=1; i < l1; i++) {
		for (int j=1; j < l2; j++) {
			if (s1[i-1] == s2[j-1]) {
				edit[i][j] = edit[i-1][j-1];
			} else {
				edit[i][j] = min(edit[i-1][j-1], edit[i-1][j], edit[i][j-1])+1;
			}
		}
	}

	for (int i=0; i < l1; i++) {
		for (int j=0; j < l2; j++) {
			printf(" %d ", edit[i][j]);
		}
		printf("\n");
	}

	return edit[l1-1][l2-1];
}

int main (int argc, char *args[]) {
	printf("\n Min edit distance = %d", editDistance("delete", "leet"));
}