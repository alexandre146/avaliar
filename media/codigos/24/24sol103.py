fatorial = int(input())
resultado = 1
while(fatorial != -1):
	while(fatorial > 0):
		resultado *= fatorial
		fatorial -= 1
	print(resultado)
	resultado = 1
	fatorial = int(input())
