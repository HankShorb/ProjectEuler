def is_palindrome(string):
	start = 0
	end = len(string)-1
	string[start] == 0
	string[end] == 0
	while(string[start] is string[end] and start<end):
		start+=1
		end-=1
	return start>=end

total = 0
for n in range(1,10**6):
	if is_palindrome(str(n)) and is_palindrome(str(bin(n))[2:]):
		total+=n

print total