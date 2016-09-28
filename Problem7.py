primes = [-1]*10001
primes[0] = 2
primes[1] = 3

counter = 2
num = 5
last = 3

while(counter<10001):
	is_prime = True
	i = 0
	while(primes[i] != -1):
		if num%primes[i]==0:
			is_prime = False
			break
		i += 1
	if(is_prime):
		primes[counter]=num
		counter += 1
	num += 2

print primes[10000]