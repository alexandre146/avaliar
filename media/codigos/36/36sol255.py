M = int(input())
N = int(input())
cont = 0
for i in range(M, N + 1):
    if(i % M == 0):
        if(cont == 0):
            maior = i
            cont += 1
        else:
            if(i > maior):
                maior = i
if(cont == 0):
    print("sem multiplos menores que", N)
else:
    print(maior)
