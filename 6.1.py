
def getPentagonalNumber (n):
    i = 1
    while i <= n :
        num = i*(3*i-1)//2
        
        if i % 10 == 0:
            print (format(num, "10d"))
        else:
            print (format(num, "10d"), end = (" "))
        i += 1
    return num
   
getPentagonalNumber(50)

