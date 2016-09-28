def is_prime(n):
	for i in range(2,n/2):
		if n%i == 0:
			return False
	return True

def smallest_prime_factor(n):
	if n%2==0:
		return 2
	i=3
	while(i<=n/2):
		if n%i==0 and is_prime(i):
			return i
		i += 2
	return n

def largest_prime_factor(n):
	temp = n
	last = 1
	while(temp!=1):
		last = smallest_prime_factor(temp)
		temp /= last
	return last

print largest_prime_factor(600851475143)