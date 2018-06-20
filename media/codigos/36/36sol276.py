x = 1
m = int(input())
n = int(input())
multiplo = m * x
maior = multiplo
if(multiplo <= n):
    while(multiplo <= n):
        x += 1
        if(multiplo > maior):
            maior = multiplo
        multiplo = m * x
    print(maior)
else:
    print("sem multiplos menores que ",n)

