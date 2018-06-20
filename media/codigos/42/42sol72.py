I = int(input())
if I < 16:
    print ("nao eleitor")
elif I >= 18 or I <= 65:
    print ("eleitor obrigatorio")
elif I > 16 and I < 18 or I > 65:
    print ("eleitor facultativo")
