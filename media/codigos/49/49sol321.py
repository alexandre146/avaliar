a = float (input())
b = float (input())
c = float (input())
if (a + b > c and a + c > b and b + c > a):
     if (a == b or c == a or c == b):
          if (b != c or c != b or a != b):
               print ("isoceles")
          else:
               print ("equilatero")
     else:
          print ("escaleno")
else:
     print ("nao e triangulo")
