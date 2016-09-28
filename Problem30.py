def digits_of_num(n):
	digits = []
	digit_place = 1
	while n/digit_place > 9:
		digit_place*=10

	while n != 0:
		digits.append(n/digit_place)
		n = n%digit_place
		digit_place /= 10
	return digits

def sum_fifth_powers(numbers):
	total = 0
	for i in range(0,len(numbers)):
		total += numbers[i]**5
	return total

numbers = []
for n in range(10,295246):
	if n == sum_fifth_powers(digits_of_num(n)):
		numbers.append(n)

print numbers
print sum(numbers)