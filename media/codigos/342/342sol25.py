
a=int(input())
b=0
for i in range ( 1 , a+1):
	if a%i==  0:
		if i%3 == 0:
			b = b +1
if b == 0:
	print ("O numero nao possui divisores multiplos de 3!")
else:
	print (b)
