num1 = int(input())
num2 = int(input())

if num1 > num2:
    aux = num1
    num1 = num2
    num2 = num1

while num1 <= num2:
    if num1%2 != 0:
        print(num1)
    num1 = num1 + 1
