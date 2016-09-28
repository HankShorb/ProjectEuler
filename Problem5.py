def lcm(x,y):
	minimum = min(x,y)
	tempx = x
	tempy = y
	for i in range(0,minimum-1):
		while tempx%(minimum-i)==0 and tempy%(minimum-i)==0 and tempx!=1:
			tempx /= minimum-i
			tempy /= minimum-i
	return tempx*y


smallest = 1

for i in range(2,21):
	smallest = lcm(smallest,i)
	print i, smallest

print smallest