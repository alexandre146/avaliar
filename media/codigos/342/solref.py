N = int(input())
j = 0
for i in range(1, N+1):
    if (N % i == 0) and (i % 3 == 0) :
        j += 1

if (j > 0) :
    print(j)
else:
    print("O numero nao possui divisores multiplos de 3!")
