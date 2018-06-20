numero = int(input())
teto = int(input())
multiplo = 1
i = 1

if teto >= numero :
    while multiplo < teto :
        multiplo = numero * i
        i += 1
    resposta = multiplo - numero
    if resposta == 0 :
        print (multiplo)
    else :
        print (resposta)
else :
    print ("sem multiplos menores que N")
