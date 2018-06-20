x=input().split()
n=int(x[0])
m=int(x[1])
if(m%n==0):
    print(m)
elif(m%n!=0):
    x=m%n
    if((m-x)==n):
        print("sem multiplos menores que "+str(m))
    else:
        print(m-x)
    

