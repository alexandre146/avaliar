quant = 0
maior = 0

m = int(input())
n = int(input())

for i in range(m, n + 1):
    if(i % m == 0):
        if(quant == 0):
            maior = i
            quant+= 1
        else:
            if(i > maior):
                maior = i
if(quant == 0):
    print("sem multiplos menores que", n)
else:
    print(maior)
    





              
            
    
    
