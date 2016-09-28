def t_num(n):
	#returns nth triangular number
	return n*(n+1)/2


#generates a list of prime numbers
primes = []
primes.append(2)
primes.append(3)

num = 5
while(len(primes)<5000):
	is_prime = True
	for i in range(0,len(primes)):
		if num%primes[i] == 0:
			is_prime = False
			break
	if(is_prime):
		primes.append(num)
	num += 2

def num_factors(n):
	#returns the number of factors of n
	factors = [0]*len(primes)
	temp = n
	i = 0

	while temp!=1:
		while temp%primes[i] == 0:
			temp /= primes[i]
			factors[i] +=1
		i += 1

	fact = 1
	for i in range(0,len(factors)):
		fact *= factors[i] + 1

	return fact

found = False
n = 1
while not found:
	tri_num = t_num(n)
	if num_factors(tri_num)>=500:
		found = True
	n += 1

print tri_num, n-1