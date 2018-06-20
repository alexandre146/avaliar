a = float (input ()) 
b = float (input ()) 
c = float (input ())

if a == b == c:
    print ('equilatero')
    
elif (a == b != c) or (b == c != a) or (a == c != b):
    print ('isoceles')

else:
    print ('escaleno')