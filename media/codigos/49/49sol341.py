a = float (input())
b = float (input())
c = float (input())
if (( a == b and b != c) or ( a == c and c != b) or (b == c and c != a)):
     print ("isoceles")
elif ( a == b and b == c):
     print ("equilatero")
else:
     print ("escaleno")
