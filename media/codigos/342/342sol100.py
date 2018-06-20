quant = 0
num = int(input())
for i in range(num):
    if(i%3 == 0):
        quant+=1
if(quant>0):
    print(quant)
else:
    print("O numero nao possui divisores multiplos de 3!")
    
