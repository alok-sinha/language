#include <stdio.h>
#include <stdlib.h>

#define N 10000

int main (int argc, char *argv[]) 
{

    if (argc != 2) {
        printf("\n Incorrect syntax ..");
        return 0;
    }

    int n = atoi(argv[1]);

    char primes[n];

    for (int i=2; i < n; i++) {
        primes[i] = 1;
    }

    for (int i=2; i < n; i++) {
        if (primes[i]) {
            for (int j=i*i; j < n; j=j+i) {
		primes[j] = 0;
            }
        }
    } 

    printf("\nPrimes:");
    for (int i=2; i < n; i++) {
	if (primes[i]) {
            printf(" %d ", i);
        }
    }
}

