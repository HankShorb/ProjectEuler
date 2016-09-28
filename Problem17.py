def num_to_word(n):
	word = ""

	if n == 1000:
		return "onethousand"

	if n>=100:
		word += digit_to_word(n/100)+"hundred"
		n -= (n/100)*100
		if n != 0:
			word += "and"

	if n != 0:
		if n >= 90:
			word += "ninety"
			n -= 90
		elif n >= 80:
			word += "eighty"
			n -= 80
		elif n >= 70:
			word += "seventy"
			n -= 70
		elif n >= 60:
			word += "sixty"
			n -= 60
		elif n >= 50:
			word += "fifty"
			n -= 50
		elif n >= 40:
			word += "forty"
			n -= 40
		elif n >= 30:
			word += "thirty"
			n -= 30
		elif n >= 20:
			word += "twenty"
			n -= 20
		elif n == 19:
			word += "nineteen"
			n = 0
		elif n == 18:
			word += "eighteen"
			n = 0
		elif n == 17:
			word += "seventeen"
			n = 0
		elif n == 16:
			word += "sixteen"
			n = 0
		elif n == 15:
			word += "fifteen"
			n = 0
		elif n == 14:
			word += "fourteen"
			n = 0
		elif n == 13:
			word += "thirteen"
			n = 0
		elif n == 12:
			word += "twelve"
			n = 0
		elif n == 11:
			word += "eleven"
			n = 0
		elif n == 10:
			word += "ten"
			n = 0

	if n != 0:
		word += digit_to_word(n)

	return word

def digit_to_word(n):
	if n == 1:
		return "one"
	elif n == 2:
		return "two"
	elif n == 3:
		return "three"
	elif n == 4:
		return "four"
	elif n == 5:
		return "five"
	elif n == 6:
		return "six"
	elif n == 7:
		return "seven"
	elif n == 8:
		return "eight"
	elif n == 9:
		return "nine"


total = 0
for n in range(1,1001):
	total += len(num_to_word(n))

print total