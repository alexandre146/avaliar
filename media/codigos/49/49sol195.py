l10=int(input(""))
l11=int(input(""))
l12=int(input(""))
if(l10!=l11 and l10!=l2 and l12!=l11):
    print("escaleno")
elif(l10==l11 and l11==l12):
    print("equilatero")
else:
    print("isosceles")

num10=int(input(""))
num11=int(input(""))
num12=int(input(""))
if(n10<=num11 and num10<=num12):
    print(num1)
elif(num11<=num10 and num11<=num12):
    print(num11)
elif(num12<=num10 and num12<=num11):
    print(num12)
