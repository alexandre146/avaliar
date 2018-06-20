quant=0
N=int(input())
for i in range(1,N+1):
    if(N%i==0):
        if(i%3==0):
            quant+=1
if(quant==0):
    print("O numero nao possui divisores multiplos de 3!\n")
else:
    print(quant,"\n")
