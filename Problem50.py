MAX = 1000000

def primesBelow(max_n):
	#sundaram sieve
    numbers = range(3, max_n+1, 2)
    half = (max_n)//2
    initial = 4

    for step in xrange(3, max_n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)

primes = primesBelow(MAX)

maximum = 0

def sum_num(num,length):
	sum = 0
	for k in range(0,length):
		sum+=primes[num+k]
	return sum

for i in range(0,len(primes)-1):
	summ = 0
	length = maximum + 1
	while summ<MAX and i+maximum<len(primes)-1:
		summ = sum_num(i,length)
		if (summ in primes):
			maximum = length
			num = i
		length+=1

print "number", sum_num(num,maximum), "starting at", primes[num], "length", maximum


"""primes = [-1]*30001
primes[0] = 2
primes[1] = 3

counter = 2
num = 5
last = 3

while(counter<30001):
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
	if primes[counter-1]>1000000:
		break

print primes[counter-1], counter-1"""