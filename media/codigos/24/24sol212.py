soma=0
a=True
while a:
	n=int(input())
	x=n
	if n==-1:
		break
	elif n==0:
		print("1")
	elif n==1:
		print("1")
	elif n==2:
		print("2")
	else:	
		while n>2:
			a=x*(n-1)
			soma=a
			x=soma
			n-=1
		print (soma)
	
