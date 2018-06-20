quant = 0
numero = int(input())
for x in range(1,numero+1):
    if(numero%x == 0):
        if(x%3 == 0):
            quant += 1
if(quant == 0):
    print("O numero nao possui divisores multiplos de 3!")
else:
    print(quant)
        
        
