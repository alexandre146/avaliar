n = int(input())
m = int(input())
for a in range(n,m,2):
    if n%2!=0:
        print (a)
for b in range(n+1,m,2):
    if n%2==0:
        print (b)
