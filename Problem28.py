total = 1
current = 1
increment = 2

while increment < 1001:
	for i in range(0,4):
		current += increment
		total += current
		
	increment += 2

print total