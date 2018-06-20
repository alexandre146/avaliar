n1 = int(input( ))
n2 = int(input( ))
n3 = int(input( ))
if(n1 + n2 > n3):
    if(n1 == n2 and n1 == n3):
        print("Equilátero")
    elif(n1 == n2 or n2 == n3 or n1 == n3):
         print("Isósceles")
    elif(n1 != n2 and n3 or n2 != n1 and n3 or n1 != n3):
         print("Escaleno")
else:
    print("É impossivel ser um triângulo")
    


