def is_palindrome(n):
	string = str(n)
	for i in range(0,len(string)/2):
		if string[i] != string[len(string)-(i+1)]:
			return False
	return True

def palindrome_list(max):
	group = []
	for i in range(1,max+1):
		if is_palindrome(i):
			group.append(i)
	return group

def largest_palindrome_product(max):
	group = palindrome_list(max)
	group = group[::-1]
	for i in range(0,len(group)):
		for j in range(1,1000):
			if group[i]%j == 0 and (group[i]/j)/100 >0 and (group[i]/j)/1000 == 0:
				return group[i]
	else:
		return 0

print largest_palindrome_product(1000000)