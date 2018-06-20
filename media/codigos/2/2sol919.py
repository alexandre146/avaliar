import sys

num1=int(input())
num2=int(input())
num3=int(input())

if num1<num2 and num2<num3:
    sys.stdout.write(str(num1)+"\n"+str(num2)+"\n"+str(num3)+"\n")
elif num1<num3 and num3<num2:
    sys.stdout.write(str(num1)+"\n"+str(num3)+"\n"+str(num2)+"\n")
elif num2<num1 and num1<num3:
    sys.stdout.write(str(num2)+"\n"+str(num1)+"\n"+str(num3)+"\n")
elif num2<num3 and num3<num1:
    sys.stdout.write(str(num2)+"\n"+str(num3)+"\n"+str(num1)+"\n")
elif num3<num2 and num2<num1:
    sys.stdout.write(str(num3)+"\n"+str(num2)+"\n"+str(num1)+"\n")
else:
    sys.stdout.write(str(num3)+"\n"+str(num1)+"\n"+str(num2)+"\n")