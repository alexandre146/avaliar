a = int(input())
b = int(input())
while(a <= b):
	if(a%3==0 and a%2!=0) or (a%3!=0 and a%2!=0):
		print(a)
		a += 1
	else:
		a += 1
	
	