x = 1
M = int(input())
N = int(input())
multiplo = M * x
maior = multiplo
if(multiplo <= N):
    while(multiplo <= N):
        x += 1
        if(multiplo > maior):
            maior = multiplo
        multiplo = M * x
    print(maior)
else:
    print("sem multiplos menores que",N)
