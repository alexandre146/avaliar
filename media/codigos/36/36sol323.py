numero = int(input())
teto = int(input())
multiplo = 1
i = 1

while multiplo < teto :
    multiplo = numero * i
    i += 1

if multiplo != 1 :
    if multiplo != teto :
        print (multiplo-numero)
    else :
        print (multiplo)
else :
    print ("sem multiplos menores que N")
