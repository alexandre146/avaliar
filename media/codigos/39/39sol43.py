cX, y = map(int,input().split())
if 	X > 0 and y > 0:
	print("primeiro")
if X < 0 and y> 0:
	print ("segundo")
if X < 0 and y < 0:
	print("terceiro")
if  X > 0 and y < 0:
	print("quarto")
if X == 0 and y != 0:
	print("eixo y")
if X != 0 and y == 0:
	print("eixo x")
if X == 0 and y == 0:
	print("origem")
