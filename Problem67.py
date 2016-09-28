input_file = open("triangle_text2.txt", "r")

triangle = []
next_line = input_file.readline()

while next_line != "":
	next_line = next_line.split()

	to_place = [0]*len(next_line)
	for i in range(0,len(next_line)):
		to_place[i] = int(next_line[i])

	triangle.append(to_place)

	next_line = input_file.readline()


def max_add(i,j):
	#Adds the larger of the two children of node i,j
	if i+1<len(triangle):
		triangle[i][j] += max(triangle[i+1][j],triangle[i+1][j+1])

for i in range(0,len(triangle)):
	for j in range(0,len(triangle[len(triangle)-1-i])):
		max_add(len(triangle)-1-i,j)
"""
for i in range(0,len(triangle)):
	for j in range(0,len(triangle[i])):
		print triangle[i][j],
	print ""
"""
print triangle[0][0]