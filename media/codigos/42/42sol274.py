eleitor=int(input())
if eleitor<16:
	print("nao eleitor")
if 18<=eleitor<=65:
	print("eleitor obrigatorio")
if 16<eleitor<18 or eleitor>65:
	print("eleitor facultativo")