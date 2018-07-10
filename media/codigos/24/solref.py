n = int(input())
while (n >= 0):
    fatorial = 1
    for i in range(1, n+1) :
        fatorial = fatorial * i
    print(fatorial)
    n = int(input())
