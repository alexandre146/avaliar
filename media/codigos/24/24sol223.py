fatorial = 1
cont = 1
while cont != -1:
    fatorial = 1
    cont = 1
    cont = int(input())
    while cont > 1:
        fatorial *= cont
        cont -= 1
    if cont >= 0:
        print(fatorial)


