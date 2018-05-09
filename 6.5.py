num1, num2, num3 = eval(input("Enter three number,divide by , " ))

def displaySortedNumber(num1, num2, num3):
    while num1>num2 or num2>num3:
        if num1 > num2:
            num1, num2 = num2, num1
        elif num2 > num3:
            num2, num3 = num3, num2
    print(str(num1)+" "+ str(num2)+" "+ str(num3))
displaySortedNumber(num1, num2, num3)