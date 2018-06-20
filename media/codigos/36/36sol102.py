a=int(input())
b=int(input())
g=0
x=0
if a>0 and b>0:
    for i in range(a,100000,a):
        if i<b:
            g=i
    if g==0:
        print("sem multiplos menores que",b)
    else:
        print(g)
