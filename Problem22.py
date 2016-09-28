def quick_sort(group,p,r):
	if p < r:
		q = partition(group,p,r)
		quick_sort(group,p,q-1)
		quick_sort(group,q+1,r)

def partition(group,p,r):
	x = group[r]
	i = p-1
	for j in range(p,r):
		if group[j] < x:
			i += 1
			temp = group[j]
			group[j] = group[i]
			group[i] = temp
	temp = group[i+1]
	group[i+1] = group[r]
	group[r] = temp
	return i+1

def name_score(string, i):
	score = 0
	for j in range(0,len(string)):
		letter_value = alpha.find(string[j])
		if letter_value > 0:
			score += letter_value
	score *= i+1
	return score

alpha = "0abcdefghijklmnopqrstuvwxyz"
input_file = open("names.txt", "r")
names = input_file.read().lower()
names = names.split(",")

quick_sort(names,0,len(names)-1)


score = 0
for i in range(0,len(names)):
	score += name_score(names[i],i)

print score