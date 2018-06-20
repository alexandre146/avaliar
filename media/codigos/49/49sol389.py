a = -1
b = -1
c = -1

a = int( input())
b = int( input())
c = int( input())

if (a == b) & (b == c):
	print("equilatero")
elif (a != b) & (b != c) & (a != c):
	print("escaleno")
else:	
	print("isosceles")
