idade = int(input())

if idade < 16:
	print("nao eleitor")
elif idade >= 16 and idade < 18:
	print("eleitor facultativo")
elif idade >= 18 and idade <= 65:
	print("eleitor obrigatorio")
else:
	print("eleitor facultativo")

