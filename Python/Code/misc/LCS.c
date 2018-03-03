#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int findLCS (const char *s1, const char *s2) 
{	
	int len1, len2;

	len1 = strlen(s1);
	len2 = strlen(s2);

	int lcs[len1+1][len2+1];
	char sequence[len1+1][len2+1][len1 > len2 ? len1+1 : len2 + 1];

	
	memset(sequence, 0, (len1+1)*(len2+1)*sizeof(char));
	memset(lcs, 0, (len1+1)*(len2+1)*sizeof(int));


	for (int i=1; i <= len1; i++) {
		for (int j=1; j <= len2; j++) {

			if (s1[i-1] == s2[j-1]) {
				sequence[i][j] = s1[i-1];
				lcs[i][j] = lcs[i-1][j-1] + 1;
			} else {

				if (lcs[i-1][j] > lcs[i][j-1]) {
					sequence[i][j] = sequence[i-1][j];
					lcs[i][j] = lcs[i-1][j];
				} else {
					sequence[i][j] = sequence[i][j-1];
					lcs[i][j] = lcs[i][j-1];
				}
			}
		}
	}
	printf("LCS: %c", sequence[len1][len2]);
	return lcs[len1][len2];
}

int main (int argc, char *args[]) {

	printf("Max len : %d", findLCS("delete", "delete"));

}


