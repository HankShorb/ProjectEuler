primes = []
primes.append(2)
primes.append(3)

counter = 2
num = 5
last = 3
total = 5

while(num<2000000):
	is_prime = True
	two = 0b1
	i = 0
	while primes[i]<=num**(0.5) and i<len(primes):
		if num%primes[i]==0:
			is_prime = False
			break
		i += 1

	if(is_prime):
		primes.append(num)
		total += num


	if two == 0b1:
		num += 2
	else:
		num += 4

	two ^= 0b1

print primes[0:10]
print primes[len(primes)-1]
print total
print sum(primes)