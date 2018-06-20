a = int(input())
c = int(input())
d = int(input())
b = a
fatorial = 1
while b > 0:
    fatorial = fatorial*b
    b = b - 1   
print (a, fatorial)
b = c
fatorial = 1
while b > 0:
    fatorial = fatorial*b
    b = b - 1   
print  (c, fatorial)
b = d
fatorial = 1
while b > 0:
    fatorial = fatorial*b
    b = b - 1   
print (d, fatorial)
if b<=0:
    print ()
