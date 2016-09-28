primes = []
primes.append(2)
primes.append(3)

num = 5
while(num<15000):
	is_prime = True
	for i in range(0,len(primes)):
		if num%primes[i] == 0:
			is_prime = False
			break
	if(is_prime):
		primes.append(num)
	num += 2

def factors(n):
	#returns the number of factors of n
	factors = [0]*len(primes)
	temp = n
	i = 0

	while temp!=1:
		while temp%primes[i] == 0:
			temp /= primes[i]
			factors[i] +=1
		i += 1

	return factors

def d(n):
	fact = factors(n)
	product = 1
	for i in range(0,len(fact)):
		if fact[i] > 0:
			sum = 0
			for k in range(0,fact[i]+1):
				sum += primes[i]**k
			product *= sum
	return product-n

amicable_numbers = []
for n in range(2,10001):
	if d(d(n)) == n and d(n) != n:
		amicable_numbers.append(n)

print sum(amicable_numbers)