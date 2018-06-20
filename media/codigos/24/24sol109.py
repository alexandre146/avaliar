numero = int(input())
contadorFatorial = numero
contadorFatorial -= 1
 
while(numero >= 0):
    if(numero >= 0 and numero <= 12):
        while(contadorFatorial > 1):
            numero *= contadorFatorial
            contadorFatorial -= 1
        print(numero)
    numero = int(input())
    contadorFatorial = numero
    contadorFatorial -= 1
