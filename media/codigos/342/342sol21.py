x=int(input(''))
c=0
for i in range(1,x+1,1):
    if x%i==0:
        if i%3==0:
            c+=1
if c!=0:
    print(c)
else:
    print('O numero nao possui divisores multiplos de 3!')

