l1 = int(input())
l2 = int(input())
l3 = int(input())
if l1 == l2 == l3:
	print('equilatero')
elif l1 == l2 or l1 == l3 or l2 == l3:
	print ('isosceles')
else:
	print ('escaleno')