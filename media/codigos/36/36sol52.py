

m = int(input())
n = int(input())
maior = 0
for item in range(m, n + 1):
    if(item % m == 0):
        if item > maior:
            maior = item
            
if maior > 0:
    print(maior)
else:
    print("sem multiplos menores que", n)
