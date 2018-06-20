num1 = int(input())
num2 = int(input())

cont = num1
contMultiplo = 0

if (num1 < num2):
    while (cont <= num2):
        if (cont % num1 == 0):
            maior = cont
            contMultiplo += 1
        cont += 1

if (contMultiplo == 0):
    print("sem multiplos menores que", num2)
else:
    print(maior)
        
