Num1 = int (input())
Num2 = int (input())
Num3 = int (input())
if (Num1>Num2) and (Num1>Num3):
    if (Num2>Num3):
        print (Num3)
        print (Num2)
        print (Num1)
    else:
        print (Num2)
        print (Num3)
        print (Num1)
elif (Num2>Num1) and (Num2>Num3):
    if (Num1>Num3):
        print (Num3)
        print (Num1)
        print (Num2)
    else :
        print (Num1)
        print (Num3)
        print(Num2)
else:
    if (Num2>Num1):
        print (Num1)
        print(Num2)
        print(Num3)
    else:
        print (Num2)
        print(Num1)
        print(Num3)

