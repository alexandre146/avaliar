n = -1

n = int(input())

if (n < 16):
	print ("nao eleitor")
elif (n >= 18) & (n <= 65):
	print("eleitor obrigatorio")
else:
	print("eleitor facultativo")
