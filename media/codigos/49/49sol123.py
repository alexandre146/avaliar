a = int(input())
b = int(input())
c = int(input())
if a==b and b==c:
    print("equilatero")
elif a==b or b==c or a==c:
    print("isosceles")
else:
    print("escaleno")
