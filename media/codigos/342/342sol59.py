quant = 0
nume = int(input())
for n in range(1,nume+1):
    if(nume%n == 0):
        if(n%3 == 0):
            quant+=1
if(quant != 0):
    print(quant)
else:
    print("O numero nao possui divisores multiplos de 3!")

        
        
