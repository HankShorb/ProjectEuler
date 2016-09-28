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

product = "1"
for i in range(1, 101):
	product = multiply_rev_nums(product,str(i)[::-1])

print product[::-1]
total = 0
for i in range(0,len(product)):
	total += int(product[i])
print total