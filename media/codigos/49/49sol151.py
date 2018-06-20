
a = float(input())
b = float(input())
c = float(input())

if (a != b) & (b == c):
    print('equilatero')
elif (a != b) & (b != c) & (a != c):
    print('escaleno')
else:
    print('isosceles')
