a = float(input())
b = float(input())
c = float(input())
if a >= b and a >= c:
	maior = a
	if b >= c:
		meio = b
		menor = c
	else: 
		meio = c
		menor = b
	print(menor,meio,maior)
elif b >= a and b >= c:
	maior = b
	if a >= c:
		meio = a
		menor = c
	else:
		meio = c
		menor = a
	print(menor,meio,maior)
elif c >= a and c >= b:
	maior = c
	if b >= a:
		meio = c
		menor = a
	else:
		meio = a
		menor = c
	print(menor,meio,maior)
