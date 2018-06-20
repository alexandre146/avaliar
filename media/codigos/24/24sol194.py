while True:
	num=int(input())
	aux=num-1
	if num == -1:
		print("")
		break
	
	while aux >= 1:
		num=num*aux
		aux=aux-1
	print(num)