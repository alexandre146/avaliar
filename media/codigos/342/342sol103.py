num = int(input( ))
quant = 0

while(num % 3 == 0):
    for i in range(1,num+1):
        if(num % i == 0):
            quant += 1
            print( quant )
        else:
            print( )
    num -= 1
    
