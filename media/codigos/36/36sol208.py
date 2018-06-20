num1=int(input())
num2=int(input())

if(num1>num2):
    multiplo= num1-1
    divisao= multiplo/num2
    if(divisao>num2):
        print("Sem multiplos menores que",num2)
    elif (divisao<=num2):
        print(multiplo)        

elif(num2>num1):
    multiplo= num2-1
    divisao= multiplo/num1
    if(divisao>num1):
        print("Sem multiplos menores que",num1)        
    elif (divisao<=num1):
        print(multiplo)        
            
        

   
