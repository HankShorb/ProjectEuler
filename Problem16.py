calculated_powers = {}

def power(num, exponent):
	if exponent == 1:
		return num
	elif (num, exponent) in calculated_powers:
		return calculated_powers[(num, exponent)]
	else:
		value = multiply_rev_nums(power(num,exponent/2),power(num,exponent-exponent/2))
		calculated_powers[(power, exponent)] = value
		return value

def multiply_rev_nums(num1, num2):
	to_add = []
	for i in range(0,len(num1)):
		for j in range(0,len(num2)):
			product = str(int(num1[i])*int(num2[j]))
			for k in range(0,i+j):
				product += "0"
			product = product[::-1]
			to_add.append(product)

	current = "0"
	for i in range(0, len(to_add)):
		current = sum_rev_nums(current, to_add[i])

	return current


def sum_rev_nums(num1,num2):
	if len(num1)>len(num2):
		while len(num1)>len(num2):
			num2 += "0"
	elif len(num2)>len(num1):
		while len(num2)>len(num1):
			num1 += "0"

	answer = ""

	carry = False
	for i in range(0,len(num1)):

		k = int(num1[i])+int(num2[i])
		if carry:
			k += 1
			carry = False

		answer += str(k%10)

		if k/10 > 0:
			carry = True
	if carry:
		answer += "1"

	return answer

result = power("2",1000)[::-1]
sum = 0
for i in range(0,len(result)):
	sum += int(result[i])

print sum