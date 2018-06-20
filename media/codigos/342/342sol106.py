quant = 0
N = int(input( ))
for a in range(1, N+1):
    if(N%3 == 0):
        if(a%3 == 0):
            quant += 1
if(quant!= 0):
    print (quant)
else:
    print ("O numero nao possui divisores multiplos de 3!")
