quant = 0
numero = int(input())
for i in range(1,numero + 1):
    if(numero % i == 0):
        if(i % 3 == 0):
            quant += 1
if(quant != 0):
    print(quant)
else:
    print("O numero nao possui divisores multiplos de 3!")


