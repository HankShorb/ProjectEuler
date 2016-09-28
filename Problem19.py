MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6

def future_day(current_day, days_to_pass):
	return (current_day+days_to_pass)%7

def count_days(start_year, end_year, start_day, day_to_count):
	count = 0
	if start_day == day_to_count:
		count += 1
	return c_days(start_year, end_year, start_day, day_to_count, count)

def c_days(year, end_year, day, day_to_count, count):
	#return the total count once we reach the end
	if year >= end_year:
		return count

	month = 1
	while month <= 12:
		
		if day == day_to_count and year >= 1901:
			count +=1
		
		#calculates starting day of the next month depending on month and year
		if month == 2:
			if year%4 == 0 and (year%100 != 0 or year%400 == 0):
				day = future_day(day, 29)
			else:
				day = future_day(day, 28)
		elif month == 4 or month == 6 or month == 9 or month == 11:
			day = future_day(day, 30)
		else:
			day = future_day(day, 31)

		
		month += 1

	return c_days(year+1, end_year, day, day_to_count, count)

print count_days(1900, 2001, MONDAY, SUNDAY)