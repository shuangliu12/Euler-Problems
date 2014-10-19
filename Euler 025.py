'''The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?'''





pa=1
pb=1

answer = 0
n = 2

while len(str(answer)) < 1000:
	answer = pa + pb
	pa = pb
	pb = answer
	n = n+1
	
	
print n, answer


'''def fibo(i):
	if i == 1:
		return 1
	elif i == 2:
		return 1
	else:
		return fibo(i-1)+fibo(i-2)'''
		

 		


