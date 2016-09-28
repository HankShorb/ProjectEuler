prev = 0
curr = 1
next = 1

term_num = 1

while len(str(curr))<1000:
	next = curr + prev
	prev = curr
	curr = next
	term_num += 1

print term_num