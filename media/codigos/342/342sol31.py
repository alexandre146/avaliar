numero = int(input())
divisoresDivisiveis = 0
for cont in range (1,numero+1):
    if (numero % cont == 0):
        if (cont % 3 == 0):
            divisoresDivisiveis += 1
if (divisoresDivisiveis == 0):
    print("O numero nao possui divisores multiplos de 3!")
else:
    print(divisoresDivisiveis)
