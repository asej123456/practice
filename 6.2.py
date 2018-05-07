m = input("Enter your integer : ")
n = eval(m)
length = len(m)

def Digits(n):
     k = 10
     digit = 0
     for i in range(n+1) :
         digit += n % k
         n -= n % k
         n //= 10
     print (digit)
         
Digits(n)