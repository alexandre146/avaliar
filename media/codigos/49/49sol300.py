a = float(input())
b = float(input())
c = float(input())
if (a + b > c and a + c > b and b + c > a):
     if (a == b and a== c):
          print ("equilatero")
     elif(a == b or b == c or  a == b):
          print ("isoceles")
     elif (a != b and b!= c and a!=c):
          print ("escaleno")
     
