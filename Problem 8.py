for a in range(1,34):
	for b in range(a,34):
		for c in range(b,34):
			if a**2 + b**2 + c**2 == 1000:
				print a, b, c
				print a*b*c