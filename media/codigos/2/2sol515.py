n1=int(input(""))
n2=int(input(""))
n3=int(input(""))

if (n1 < n2) and (n1 <n3):
    rn1=n1
elif n2<n1 and n2 <n3:
    rn1=n2
else:
    rn1=n3

if n2 > n1 and n2 < n3 or (n2 > n3 and n2 < n1) :
    rn2=n2
elif (n3 > n1 and n3 < n2) or (n3 > n2 and n3 < n1):
    rn2=n3
else:
    rn2=n1

if n1 < n3 and n2 < n3:
    rn3=n3
elif n2 > n1 and n2 > n3:
    rn3=n2
else:
    rn3=n1
    

print(rn1)
print(rn2)
print(rn3)
