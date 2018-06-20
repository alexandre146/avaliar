
num = int(input());
while num >= 1:
    resultado = 1
    lista = range(1,num+1)
    for x in lista:
        resultado = x * resultado
        print(resultado)
    num = int(input());