
quant=0
numN=int(input())
for x in range(1,numN+1):
    if(numN%x==0):
        if(x%3==0):
            quant+=1
if(quant==0):
    print("O numero nao possui divisores multiplos de 3!\n")
else:
    print(quant,"\n")

