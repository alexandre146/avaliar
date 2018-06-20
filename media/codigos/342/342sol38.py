num = int(input())
quantDivisores = 0


for divisores in range(1,num +1):
    if(num % divisores == 0):
        if(divisores % 3 == 0):
            quantDivisores += 1
            
if(quantDivisores > 0):
    print(quantDivisores)
    
else:
    print("O numero nao possui divisores multiplos de 3!")
