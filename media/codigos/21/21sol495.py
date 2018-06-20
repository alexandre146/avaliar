print("Digite um número:")
numero1=int(input())
print("Digite outro número:")
numero2=int(input())
numero=0
if (numero1>numero2):
    numero=numero2
    if (numero2%2==1):
        print(numero2)
    while( numero<numero1):
        numero=numero+1
        if(numero%2==1):
            print(numero)
elif (numero1<numero2):
    numero=numero1
    if (numero1%2==1):
        print(numero1)
    while (numero<numero2):
        numero=numero+1
        if(numero%2==1):
            print(numero)

