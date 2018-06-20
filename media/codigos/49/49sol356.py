a = float (input())
b = float (input())
c = float (input())
if (a + b > c and b + c > a and a + c > b):
     if (a == b != c or b == c != a or c == a != b):
          print ("isoceles")
     elif (a == b and b == c and c == a):
          print ("equilatero")
     else:
          print ("escaleno")
     
   
   
