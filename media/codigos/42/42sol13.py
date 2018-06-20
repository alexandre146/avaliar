idade = int(input())
if idade < 16:
    n1 = ("não eleitor")
    print (n1)
elif 65 < idade >= 18:
    n2 = ("eleitor obrigatorio")
    print (n2)
else:
    n3 = ("eleitor facultativo")
    print (n3)
