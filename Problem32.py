def identity_is_pandigital(n):
	for i in range(1,99):
		if n%i == 0:
			digits = []
			digits += digits_of_num(i)
			digits += digits_of_num(n/i)
			digits += digits_of_num(n)
			digits.sort()
			if digits == [1,2,3,4,5,6,7,8,9]:
				return True
	return False

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

unusuals = []

for n in range(1234,9876):
	string = str(n)
	if not "0" in string:
		if identity_is_pandigital(n):
			unusuals.append(n)


print unusuals
print sum(unusuals)