m=int(input())
n=int(input())
maiorMultiplo=0
cont=m
while(cont<=n):
    if(cont%m == 0):
        if(cont>=maiorMultiplo):
            maiorMultiplo=cont
    cont+=1
if(maiorMultiplo==0):
    print("sem multiplos menores que",n,)
else:
    print(maiorMultiplo)

        
        
