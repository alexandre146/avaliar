num1 = int(input())
num2 = int(input())
num3 = int(input())
pnum = 0
snum = 0
tnum = 0
if(num1 >= num2 & num1 >= num3):
    pnum = num1
    if(num2 >= num3):
        snum = num2
        tnum = num3
    else:
        snum = num3
        tnum = num2
if(num2 >= num1 & num2 >= num3):
    pnum = num2
    if(num1 >= num3):
        snum = num1
        tnum = num3
    else:
        snum = num3
        tnum = num1
if(num3 >= num1 & num3 >= num2):
    pnum = num3
    if(num2 >= num1):
        snum = num2
        tnum = num1
    else:
        snum = num1
        tnum = num2
print (tnum)
print (snum)
print (pnum)
