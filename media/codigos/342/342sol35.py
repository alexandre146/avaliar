num = int(input())
quant = 0
for i in range(num):
    if(i % 3 == 0) and (i % num):
        quant+= 1
if(quant == 0):
    print("O numero nao possui divisores multiplos de 3!")
else:
    print(quant)
