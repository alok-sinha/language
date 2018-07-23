
from collections import defaultdict

def getPrimeFact(n):
	primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,47]
	powers = defaultdict(int)

	for prime in primes:
		while n % prime == 0:
			powers[prime] += 1
			n = n/prime
			if n == 1:
				return powers
	return powers


print(getPrimeFact(pow(2,5)*pow(5,3)*pow(7,2)))
