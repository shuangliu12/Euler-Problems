'''215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?'''






product = 2**1000
product=str(product)
sum=0
for i in range(0,len(product)):
	sum = sum + int(product[i])

print sum 