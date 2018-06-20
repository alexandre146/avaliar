lado1=int(input(""))
lado2=int(input(""))
lado3=int(input(""))
if(lado1!=lado2 and lado1!=lado3):
    print("escaleno")
elif(lado1==lado2 and lado2==lado3):
    print("equilatero")
else:
    print("isosceles")
