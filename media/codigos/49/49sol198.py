a = int (input ())
b = int (input ())
c = int (input ())
if (a != b and a!= c and b != c):
    print ('escaleno')
elif (a == b and b == c):
    print ('equilatero')
elif (a == b and b != c):
    print ('isóceles')
elif (c == a and a != b):
    print ('isóceles')
elif (b == c and b != a):
    print ('isoceles')
