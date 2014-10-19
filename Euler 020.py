'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27

Find the sum of the digits in the number 100!'''	

def factorial(i):
	answer = 1
	for i in range(1,i+1):
		answer = answer*i
	answer = str(answer)
	
	# count the sum
	sum = 0
	for j in range(0,len(answer)):
		sum = sum + int(answer[j])
	return sum
	
print factorial(100)