num1 = int(input())
num2 = round(num1/2)
divisor = 0
for p in range(num2,2,-1):
	if(((num1%p) == 0) and ((p%3) == 0)):
		divisor += 1
	
print(divisor)