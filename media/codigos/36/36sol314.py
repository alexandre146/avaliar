n=int(input())
m=int(input())
a=0
while m>n:
    if m%n==0:
        print(m)
        a=1
        break
    m-=1
if a==0:
    print('sem multiplos menores que %i'%m)
