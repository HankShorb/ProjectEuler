def cycle_length(d):
	computed_operations = []
	q = 1
	while q != 0:
		while q/d == 0:
			q *= 10
		sub = (q/d)*d
		q -= sub
		if q in computed_operations:
			return len(computed_operations)-computed_operations.index(q)
		else:
			computed_operations.append(q)
	return 0

maximum = 0
max_num = 0
for n in range(1,1000):
	length = cycle_length(n)
	if length > maximum:
		maximum = length
		max_num = n

print max_num