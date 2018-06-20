__author__ = 'Wellington'
n=0
i=0
j=1
fat=1
while(i<=12):
    i+=1
    n=int(input())
    if(n==-1):
        break
    
    for j in range(1, n+1):
        fat=fat*j
    print(fat)