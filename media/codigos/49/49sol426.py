x=int(input())
y=int(input())
z=int(input())

if x==z==y:
    print("equilatero\n")
elif x!=z and x!=y and z!=y:
    print("escaleno\n")
else:
    print("isosceles\n")
