num1 = int(input())
num2 = int(input())
maior = max (num1, num2)
menor = min (num1, num2)
numeros = menor
while numeros < maior :
    if numeros % 2  == 1 :
        print (numeros, "\n")
    numeros += 1
