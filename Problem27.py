primes = []
primes.append(2)
primes.append(3)

num = 5

while(num<90000):
	two = 0b1
	i = 0
	while primes[i] <= num**(0.5) and i < len(primes):
		if num%primes[i]==0:\
			break
		i += 1
	else:
		primes.append(num)

	if two == 0b1:
		num += 2
	else:
		num += 4

	two ^= 0b1

def num_primes_quad(a,b):
	n = 0
	value = b
	length = 0
	while value in primes:
		length += 1
		n += 1
		value = n**2 + a*n + b

	return length


maximum = 0
max_pair = (0,0)


for b in primes[0:168]:
	for a in range(-b,1000):
		length = num_primes_quad(a,b)
		if length > maximum:
			maximum = length
			max_pair = (a,b)
			print max_pair

print maximum, max_pair, max_pair[0]*max_pair[1]

i = 0
while primes[i]<1000:
	i += 1
print i