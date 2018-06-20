divisores= 0
cont = 1
N= int (input())
while (cont <= N):
    if (cont%3 == 0) and (N %cont == 0):
        divisores+=1
    cont+= 1
if (divisores == 0):
    print("O numero nao possui divisores multiplos de 3!")
else:
    print(divisores)
    
 
