british_currency = [200,100,50,20,10,5,2,1]

def make_change(denominations, change):
	coins_so_far = [0]*len(denominations)
	notch = 0
	list_of_changes = []
	make_change_recur(change, coins_so_far, notch, list_of_changes, denominations)
	return list_of_changes

def make_change_recur(remaining_change, coins_so_far, notch, list_of_changes, denominations):
	if remaining_change == 0:
		list_of_changes.append(duplicate(coins_so_far))
	else:
		if remaining_change > 0:
			coins_so_far[notch] += 1
			make_change_recur(remaining_change-denominations[notch], coins_so_far, notch, list_of_changes, denominations)
			coins_so_far[notch] -= 1
		if notch+1 < len(denominations):
			make_change_recur(remaining_change, coins_so_far, notch+1, list_of_changes, denominations)

def duplicate(my_list):
	dup = [0]*len(my_list)
	for i in range(0,len(my_list)):
		dup[i] = my_list[i]
	return dup

change_for_200 = make_change(british_currency, 200)
print len(change_for_200)