numero = int(input())
 
while(numero != -1):
    contadorFatorial = numero
    contadorFatorial -= 1
    while(contadorFatorial > 1):
        numero *= contadorFatorial
        contadorFatorial -= 1
    print(numero)
    numero = int(input())
























