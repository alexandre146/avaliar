idade = int(input())
if idade < 16:
    print ("não eleitor")
elif 65 < idade >= 18:
    print ("eleitor obrigatorio")
else:
    print ("eleitor facultativo")
