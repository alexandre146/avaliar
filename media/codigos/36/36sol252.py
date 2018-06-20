num1= int(input())
num2= int(input())

if(num1 < num2):
    while(num1 < num2):
        if(num1 % 5 == 2)or(num1 % 5 == 3):
            print(num1)
        num1 +=1

else:
    while(num2 < num1):
        if(num2 %5 == 2)or(num2 % 5 == 3):
            print(num2)

        num2 +=1    
