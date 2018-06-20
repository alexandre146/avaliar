number1 = int(input())
number2 = int(input())
number3 = int(input())
if (number1 > number2) and (number1 > number3) and (number2 > number3):
    print (number3)
    print (number2)
    print (number1)
if (number1 > number2) and (number1 > number3) and (number3 > number2):
    print (number2)
    print (number3)
    print (number1)
if (number2 > number1) and (number2 > number3) and (number1 > number3):
    print (number3)
    print (number1)
    print (number2)
if (number2 > number1) and (number2 > number3) and (number3 > number1):
    print (number1)
    print (number3)
    print (number2)
if (number3 > number1) and (number3 > number2) and (number1 > number2):
    print (number2)
    print (number1)
    print (number3)
if (number3 > number1) and (number3 > number2) and (number2 > number1):
    print (number1)
    print (number2)
    print (number3)
    


