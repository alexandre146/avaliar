
numero = 0
while(numero >= 0):
    numero = int(input())
    if(numero >= 0 and numero <= 12):
        contadorFatorial = numero
        contadorFatorial -= 1
        while(contadorFatorial > 1):
            numero *= contadorFatorial
            contadorFatorial -= 1
        print(numero)






