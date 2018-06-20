n1 = float(input())
n2 = float(input())
n3 = float(input())
 
if n1 == n2 == n3:
    print("equilatero")
elif n1 == n2 or n1 == n3 or n3 == n2:
    print("isosceles")
else:
    print("escaleno")         