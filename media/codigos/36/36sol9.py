m=int(input())
n=int(input())
maior=None
maior2=0
x=m
m=m+1
while m<n:
    if m%x==0:
        if m>maior2 :
            maior=m
    m=m+1
if maior!=None:
    print(maior)
else:
    print("sem multiplos menores que N")

    
    
