def gcd(a,b):
	while(a!=0 and b!=0):
		if(a>b):
			a -= b
		else:
			b -= a
	return max(a,b)

def is_dc(a,b):
	if((a%10!=0) and (b%10!=0)):
		ones_tens = (a/gcd(a,b)==(a%10)/gcd(a%10,b/10)) and (b/gcd(a,b)==(b/10)/gcd(a%10,b/10))
		tens_ones = (a/gcd(a,b)==(a/10)/gcd(a/10,b%10)) and (b/gcd(a,b)==(b%10)/gcd(a/10,b%10))
		if(a/10==b%10 and ones_tens):
			return True
		elif(a%10==b/10 and tens_ones):
			return True
	else:
		return False

numerator = 1
denominator = 1

for a in range(10,100):
	for b in range(a+1,100):
		if (is_dc(a,b)):
			numerator *= a
			denominator *= b

print denominator, numerator, denominator/gcd(denominator,numerator)