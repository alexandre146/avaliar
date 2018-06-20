m=int(input())
n=int(input())
x=0
for i in range(n+1):
    if i%m==0:
        x=i
if x!=0:
    print(x)
else:
    print("sem multiplos menores que N")