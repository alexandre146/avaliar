numero = int(input())
while numero != -1 and numero >= 0 and numero <= 12:
    if numero == 0:
        numero = 1
    else:
        valor = numero
        while valor != 1:
            valor -= 1
            numero *= valor
    print(numero)
    numero = int(input())
