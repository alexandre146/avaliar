

num = int(input());
while num >= 0 and num <= 12:
    resultado = 1
    lista = range(1,num+1)
    for x in lista:
        resultado*= x
        resultado = int(resultado)
    print(resultado)
    num = int(input());
    