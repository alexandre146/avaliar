num = int (input())
qtdeDivisores = 0
for i in range (1,num+1):
    if (num % i == 0):
        if (i % 3== 0 ):
            qtdeDivisores = qtdeDivisores + 1
if (qtdeDivisores > 0):
    print(qtdeDivisores)
else:
    print("O numero nao possui divisores multiplos de 3!" )
        
