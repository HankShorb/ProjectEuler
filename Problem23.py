primes = []
primes.append(2)
primes.append(3)

num = 5
while(num<30000):
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

def is_abundant(n):
	return d(n)>n

def abundants_up_to(n):
	abundants = []
	for i in range(1,n):
		if is_abundant(i):
			abundants.append(i)
	return abundants

abundants = abundants_up_to(28123)
non_abundant_sum = []

for n in range(1, 28123):
	i = 0
	not_abundant_sum = True
	while i<len(abundants) and abundants[i]<n and not_abundant_sum:
		if (n-abundants[i] in abundants):
			not_abundant_sum = False
		i += 1
	if not_abundant_sum:
		non_abundant_sum.append(n)


print sum(non_abundant_sum)