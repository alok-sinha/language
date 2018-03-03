#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *args[]) {

	char *filename = args[1];

	char file[32];
	scanf("\nEnter a filename to open %5s %s", file, file);
	printf("Opening file %5s", file);


	FILE *fp;
	fp = fopen(filename,"r");
	if (!fp) {
		printf("\n Can not open file for reading ");
		return -1;
	}

	char *s;
	s = (char *)malloc(128);

	s = fgets(s, 128, stdin);
	while (s != NULL) {
		printf("Read : 	%s", s);
		s = fgets(s, 128, stdin);
	}
	printf("\n Done reading...");
	fclose(fp);

}

