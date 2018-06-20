a = int(input())
b = int(input())
c = int(input())
if (a != b and a != c and b != c):
    print ('escaleno')
elif (a == b and a == c):
    print ('equilatero')
elif (a == b and b != c):
    print ('isosceles')
elif (c==a and a != b):
    print ('isosceles')
elif (b == c and b != a):
    print ('isosceles')
