

a = int (input ("Digite sua idade: "))

if a < 16:
	print ("nao eleitor")
elif a == 16 or a > 65:
    print ("eleitor facultativo")
else:
    print ("eleitor obrigatorio")
