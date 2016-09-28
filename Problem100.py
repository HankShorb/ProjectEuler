import math

def findP(n):
	check = (int)(math.ceil(n/(2**0.5)))
	if (prob(check,n) == 0):
		return check
	else:
		return -1
		#print top, bottom, p

def prob(blue,total):
	return 2*(blue**2 - blue) - (total**2 - total)

n = 10**12
blue_disc = -1
while(blue_disc == -1):
	if((n-10**12)%(10**5) == 0):
		print n
	blue_disc = findP(n)
	n += 1

print n-1, blue_disc