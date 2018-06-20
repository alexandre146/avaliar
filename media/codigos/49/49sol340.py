a = float (input())
b = float (input())
c = float (input())
if (a == b or b == c or c == a):
     if (a == b and b == c):
          print ("equilatero")
     elif (b != a or b != c or c != a):
          print ("isoceles")
else:
     print ("escaleno")
