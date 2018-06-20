

maior=0
meio=0
menor=0

valor_1 = int(input('digite valor 1: '))
valor_2 = int(input('digite valor 2: '))
valor_3 = int(input('digite valor 3: '))

if(valor_1 > valor_2 and valor_1 > valor_3):
    maior = valor_1
    if(valor_2 > valor_3):
        meio = valor_2
        menor = valor_3
elif(valor_2 > valor_1 and valor_2 > valor_3):
    maior = valor_2
    if(valor_1 > valor_3):
        meio = valor_1
        menor = valor_3
elif(valor_3 > valor_1 and valor_3 > valor_2):
    maior = valor_3
    if(valor_1 > valor_2):
        meio = valor_1
        manor = valor_2

print(maior)
print(meio)
print(menor)
