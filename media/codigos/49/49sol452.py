a = int(input())
b = int(input())
c = int(input())
if a == b == c:
	print ("equilatero")
elif a == b or a == c or c == b:
	print ("isósceles")
elif a != b != c:
	print ("escaleno")
