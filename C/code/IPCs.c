#include <stdio.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <string.h>

int main (int argc, char *args[]) {
	int fd[2];


	pipe(fd);


	pid_t pid = fork();

	if (pid > 0) {
		close(fd[0]);
		write(fd[1], "Hello from parent\n", strlen("Hello from parent\n"));

	} else {
		char line[24];
		close (fd[1]);
		int n = read(fd[0], line, 24);
		printf("\n %s %d", line, n);
	}



}