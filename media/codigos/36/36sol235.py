i=0
m=int(input())
n=int(input())
o=0
while(i<1):
    if(m<=n):    
        p=n//m
        o=m*p
        print(o)
    else:
        o="sem multiplos menores que %d" %n
    i+=1

