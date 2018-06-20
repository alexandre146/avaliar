idade = int(input())
if idade < 16:
	print("nao eleitor")
if idade == 18 and idade <= 65:
	print ("eleitor obrigatorio")
if idade >= 16 and idade < 18:
	print ("voto facultativo")
else:
	print("voto facultativo")
