num=int(input())
cont=0
quant=0
a="O numero não possui divisores de 3!"
while(cont<num):
    if(num%3==0):
        quant+=1
        

    num-=1
if(quant!=0):
    print(quant)
else:
    print(a)
