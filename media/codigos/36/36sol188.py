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
        elif(m==0):
            break
if(solucao==0):
    print("sem multiplos menores que N")
else:
    print(solucao)
