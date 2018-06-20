__author__ = 's01d'
i=0
total=1
x=int(input())
while x>=0:

    while x>=0:
        if x==0:
            total=total
        else:
            total=total*x
        x=x-1
    print(total)
    total=1

    x=int(input())