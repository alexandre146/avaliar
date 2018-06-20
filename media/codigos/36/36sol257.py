m=int(input())
n=int(input())
multiplo=0
solucao=0
cont=0
if(not m>n):
    while(solucao<n):
        cont+=1
        solucao=cont*m
        if(solucao+m>n):
            break

if(solucao==0):
    print("sem multiplos menores que %.f"%n)
else:
    print(solucao)
