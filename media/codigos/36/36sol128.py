cont = 10
num = int(input( ) )
maior = num
while(cont > 0):
    num = int(input( ) )
    if(num > maior):
        maior = num
        cont += 1
        print(maior )
    else:
        print( )
