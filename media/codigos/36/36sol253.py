num1= int(input())
num2= int(input())

cont= num1
multiplo= 0

if(num1 < num2):
    while(cont <= num2):
        if(cont % num1 == 0):
            maiorNum= cont
            multiplo +=1
        cont+=1

if(multiplo == 0):
    print("Sem multiplos menores que",num2)

else:
    print(maiorNum)
    
            
        
