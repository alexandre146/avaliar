num1=int(input())
num2=int(input())
num3=int(input())
if(num1!=num2 and num2!=num3 and num3!=num1):
    print("escaleno")
elif(num1==num2==num3):
    print("equilatero")
elif(num1==num2 or num1==num3 or num2==num3): 
    print("isosceles")
