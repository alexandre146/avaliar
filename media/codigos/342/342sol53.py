numero = int(input())
divisores = 0
for i in range(1,numero+1):

    if(numero % i == 0):
        if(i % 3 == 0):
            divisores +=1

if(divisores!=0):
    print(divisores,"\n")
else:
    print("O numero nao possui divisores multiplos de 3!\n")
