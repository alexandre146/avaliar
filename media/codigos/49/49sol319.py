a = float (input())
b = float (input())
c = float (input())
if (a + b > c and a + c > b and b + c > a):
     if (a == b and a == c):
          print ("equilatero")
     elif((a == b)!=c or (b == c) !=a or (c == a)!=b):
          print ("isoceles")
     elif (a != b and c or b != a and c or a != c): 
          print ("escaleno")
else:
     print ("nao e triangulo")
