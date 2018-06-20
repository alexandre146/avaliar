n = int(input())
o = int(input())
p = int(input())
if(n == o and o == p):
    print('equilatero')
elif( n == o and o!=p):
    print ('isosceles')
elif (o == p and o != n):
    print('isosceles')
elif (p == n and n != o):
    print('isosceles')
else:
    print ('escaleno')
