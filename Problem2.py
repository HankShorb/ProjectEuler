first = 0
second = 1
current = 0
total = 0

while(current<4000000):
	if current%2 == 0:
		total+=current
	current = first + second
	first = second
	second = current

print total