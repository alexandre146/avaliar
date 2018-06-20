n=int(input())
m=int(input())
maior=0
for i in range(0,m):
    if i%n==0:
        maior=i
if maior!=0:
    print(maior)
else:
    print("sem multiplos menores que",n)
