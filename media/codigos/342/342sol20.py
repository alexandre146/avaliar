n = int(input())

cont = 0
for i in range(3,n+1,3):
    if ( n % i == 0 ):
        cont += 1
if ( cont > 0 ):
    print (cont)
else:
    print ('O numero nao possui divisores multiplos de 3!')
