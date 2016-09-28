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

#assumes n is positive
def digit_len(n):
    length=0
    while(n>9):
        n -= n%(10**length)
        length+=1
    return length-1

def left_cycle(n):
    d_len = digit_len(n)
    ones = n%10
    n = n/10
    n += ones*(10**(d_len-1))
    return n

def is_cyclic_prime(n):
    d_len = digit_len(n)
    for i in range(1,d_len):
        n = left_cycle(n)
        if not (n in primes):
            return False
    return True

primes = primesBelow(MAX)


total = 0

for n in primes:
    if is_cyclic_prime(n):
        print n
        total+=1

print total