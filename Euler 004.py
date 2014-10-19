A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.
Find the largest palindrome made from the product of two 3-digit numbers.


def pali(num):
    str_num=str(num)
    length=len(str_num)
    for i in range(0, length//2):
        if str_num[i]!=str_num[length-1-i]:
           return False       
    return True

answer=10000
for j in range(100,1000):
    for h in range(100,1000):
        result = j*h
        if pali(result) == True:
            if result > answer:
                answer=result                        
            
print answer
