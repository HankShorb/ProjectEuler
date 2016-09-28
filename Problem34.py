fact = [1,1,2,6,24,120,720,5040,40320,362880]

def fact_d_sum(n):
	total = 0
	while(n!=0):
		total += fact[n%10]
		n = n/10
	return total

total = 0

for n in range(10,1000000):
	if(n==fact_d_sum(n)):
		total += n

print total

