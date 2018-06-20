m = int(input())
n = int(input())
maior = 0
for x in range(0,n):
    if (x%m == 0) & (x > maior):
        maior = x
print(maior)