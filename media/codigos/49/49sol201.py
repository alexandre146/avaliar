a=int(input())
b=int(input())
c=int(input())
if(a==b and b==c):
    print('equilatero')
elif(a==b and b!=c):
    print('isosceles')
elif(b==c and b!=a):
    print('isosceles')
elif(c==a and a!=b):    
    print('isosceles')
else:
    print('escaleno')
