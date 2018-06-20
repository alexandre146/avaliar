num = int(input())
x = 0
y = 0
r = 0
q = 0
for cont in range(num):
    x+=1
    if(num % x == 0):
        y+=1
for cont in range(y):
    q+=1
    if(q % 3):
        r+=1
    
if(r > 0):
    print(r)
    print()
else:
    print("O numero nao possui divisores multiplos de 3!")
    print()
