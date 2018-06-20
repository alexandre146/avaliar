num1 = input("")
num2 = input("")
num3 = input("")

if (num1 > num2) and (num1 > num3):
    if (num2 > num3):
        print (num3)
        print (num2)
        print (num1)
    else:
        print (num2)
        print (num3)
        print (num1)
if (num2 > num1) and (num2 > num3):
    if (num1 > num3):
        print (num3)
        print (num1)
        print (num2)
    else:
        print (num1)
        print (num3)
        print (num2)
if (num3 > num1) and (num3 > num2):
    if (num2 > num1):
        print (num1)
        print (num2)
        print (num3)
    else:
        print (num2)
        print (num1)
        print (num3)
else:
    print(num1)
    print(num2)
    print(num3)

