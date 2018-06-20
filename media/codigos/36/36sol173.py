m = int(input())
n = int(input())
maior = 0
for x in range(0,n+1):
    if (x%m == 0) & (x > maior):
        maior = x
if maior == 0:
    print('sem multiplos menores que %d'%n)
else:
    print(maior)
        