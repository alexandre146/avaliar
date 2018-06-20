numero1 = int(input())
numero2 = int(input())

if numero1 > numero2:
    numeros = range(numero2,numero1+1)
else:
    numeros = range(numero1,numero2+1)

for x in numeros:
    if x % 2 !=0:
        print(x)
