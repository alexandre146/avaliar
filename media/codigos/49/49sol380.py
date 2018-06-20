n1,n2,n3= int(input()),int(input()),int(input())

if n1 == n2 and n1 == n3 and n2 == n3:
    print("equilatero")
else:
    if n1 == n2 or n1 == n3 or n2 == n3:
        print("isoceles")
    else:
        print("escaleno")
