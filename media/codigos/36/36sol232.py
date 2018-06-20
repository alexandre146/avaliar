num1=int(input())
num2=int(input())
while(num1>0 and num2>0):
    if(num2>=num1):
        num3=num2//num1
        num4=num3*num1
        print(num4)
    else:
        print("sem multiplos menores que",num1)
    num1=int(input())
    num2=int(input())
    
    
    
