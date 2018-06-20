a = float(input())
b = float(input())
c = float(input())

if a==b and a==c:
    print("equilatero")
elif a!=b and a!=c and b!=c:
    print("escaleno")
else:
    print("isosceles")
    
