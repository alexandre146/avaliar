num = int(input())
quant = 1
for i in range(num + 1):
    if(i % 3 == 0) and (num % i == 0):
        quant+= 1
if(quant == 0):
    print("O numero nao possui divisores multiplos de 3!")
else:
    print(quant)
