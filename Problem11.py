grid_file = open("grid.txt", "r")
next_line = grid_file.readline()
grid = []

while next_line != "":
	grid_line = next_line.split()

	for i in range(0, len(grid_line)):
		grid_line[i] = int(grid_line[i])

	grid.append(grid_line)
	next_line = grid_file.readline()


max_h = 0 #horizontal
max_v = 0 #vertical
max_du = 0 #diagonal upwards
max_dd = 0 #diagonal downwards

"""
def max_horizontal(grid,n):
	maximum = 1
	for i in range(0,min(len(grid),1)):
		for j in range(0,min(len(grid[i]),n)):
			maximum *= grid[0][j]

    
	for i in range(0,len(grid)):
		product = 1
		for j in range(0,min(len(grid[i]),n)):
			product *= grid[0][j]

		for j in range(0,len(grid[i])-n):
			product = (product/grid[i][j])*grid[i][j+n]
			if product>maximum:
				maximum = product
				print i,j
"""

def product(group):
	product = 1
	for i in range(0,len(group)):
		product *= group[i]
	return product


def max_horizontal(grid,n):
	maximum = product(grid[0][0:n])
	current = maximum
	for i in range(0, len(grid)):
		for j in range(0,len(grid[i])-n+1):
			current = product(grid[i][j:j+n])
			if current > maximum:
				maximum = current

	return maximum


def max_vertical(grid,n):
	curr_sect = [1]*n

	for k in range(0,n):
		curr_sect[k] = grid[k][0]

	maximum = product(curr_sect)

	for i in range(0,len(grid)-n+1):
		for j in range(0,len(grid[i])):
			for k in range(0,n):
				curr_sect[k] = grid[i+k][j]
			current = product(curr_sect)
			if current>maximum:
				maximum = current

	return maximum

def max_diagonal_down(grid,n):
	curr_sect = [1]*n

	for k in range(0,n):
		curr_sect[k] = grid[k][k]

	maximum = product(curr_sect)

	for i in range(0,len(grid)-n+1):
		for j in range(0,len(grid)-n+1):
			for k in range(0,n):
				curr_sect[k]=grid[i+k][j+k]
			current = product(curr_sect)
			if current > maximum:
				maximum = current

	return maximum

def max_diagonal_up(grid,n):
	curr_sect = [1]*n

	for k in range(0,n):
		curr_sect[k]=grid[n-k-1][k]

	maximum = product(curr_sect)

	for i in range(n-1,len(grid)):
		for j in range(0, len(grid[i])-n+1):
			for k in range(0,n):
				curr_sect[k] = grid[i-k][j+k]
			current = product(curr_sect)
			if current > maximum:
				maximum = current

	return maximum


def max_product(grid,n):
	max_h = max_horizontal(grid,n)
	max_v = max_vertical(grid,n)
	max_dd = max_diagonal_down(grid,n)
	max_du = max_diagonal_up(grid,n)
	return max(max_h, max_v, max_dd, max_du)




print "vertical: ",
print max_vertical(grid,4)
print "horizontal: ",
print max_horizontal(grid,4)
print "diagonal down: ",
print max_diagonal_down(grid,4)
print "diagonal up: ",
print max_diagonal_up(grid,4)
print "max: ",
print max_product(grid,4)