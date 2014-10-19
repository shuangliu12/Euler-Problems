'''145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.'''



A=[]
# the function to calculate factorials
def fac(num):
	sum = 1
	for num in range(2, num+1):
		sum = sum*num
	return sum

# for digit 7, the biggest is 7-digit, so the answer is the at most 7-digit
temp = 0
for i in range(1,11):
	temp = temp + fac(9)
	print i, "digits: ", i,"* 9! = ", temp


for num in range(3,2540161):
	answer = 0
	num = str(num)
	for j in range(0,len(num)):
		answer = answer + fac(int(num[j]))
	if answer == int(num):
		A.append(answer)
		
print sum(A)
