'''Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.'''

x=1
y=2
current = x + y
sum = 2
while current <= 4000000:
    if current % 2 == 0:
        sum = sum + current
    x = y
    y = current
    current = x + y
print sum