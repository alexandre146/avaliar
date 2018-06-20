x=int(input())
y=int(input())
z=int(input())
if (x<y<z):
	print(x)
	print(y)
	print(z)
elif (x<z<y):
	print(x)
	print(z)
	print(y)
elif (z<x<y):
	print(z)
	print(x)
	print(y)
elif (z<y<x):
	print(z)
	print(y)
	print(x)
elif (y<x<z):
	print(y)
	print(x)
	print(z)
elif (y<z<x):
	print(y)
	print(z)
	print(x)