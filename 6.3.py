m = input("Enter your integer : ")
n = eval(m)
l = n
def Reverse(n):
    k = len(m) 
    num = 0
    i = 1
    while i <= k:
        num += ((n % 10**i)//10**(i-1))*10**(k-i)
        #print("when i is " + str(i) + " num is " + str(num) )
        #take the Sumnum
        n -= (n % 10**i)
        #print("when i is " + str(i) + " n is " + str(n))
        i += 1
    if num == l :
        print("This is a reverse number !")
    else:
        print("This is NOT a reverse number ")
Reverse(n)