def square_of_sums(n):
	return (n*(n+1)/2)**2

def diff_of_sums(n):
	diff = 0
	for i in range(1,n+1):
		for j in range(i+1,n+1):
			diff += i*j
	return diff*2

def sum_of_squares(n):
	return square_of_sums(n)-diff_of_sums(n)

print diff_of_sums(100)