input_file = open("fifty_digit_nums.txt", "r")
output_file = open("fifty_digit_sum.txt", "w")
nums = input_file.read().split()
print len(nums)
for i in range(0,len(nums)):
	nums[i] = nums[i][::-1]

"""
carries = [0]*51
for i in range(0, len(nums[0])):
	sum = 0
	for j in range(0, len(nums)):
		sum += int(nums[j][i])
	sum+=carries[i]

	output_file.write(str(sum%10))
	sum = (sum-(sum%10))/10

	carry=1
	while sum != 0 and carry+i<50:
		carries[i+carry] += sum%10
		sum = (sum-carries[i+carry])/10
		carry+=1
	carries[50]+=sum
"""

def sum_rev_nums(num1,num2):
	if len(num1)>len(num2):
		while len(num1)>len(num2):
			num2 += "0"
	elif len(num2)>len(num1):
		while len(num2)>len(num1):
			num1 += "0"

	answer = ""

	carry = False
	for i in range(0,len(num1)):

		k = int(num1[i])+int(num2[i])
		if carry:
			k += 1
			carry = False

		answer += str(k%10)

		if k/10 > 0:
			carry = True
	if carry:
		answer += "1"

	return answer

prev = "0"
print len(nums)
for i in range(0,len(nums)):
	prev = sum_rev_nums(prev,nums[i])

answer = prev[::-1]
print answer
print answer[0:10]