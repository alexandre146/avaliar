n = int(input("Coloque os numeros para serem comparados :"))
m = int(input())

if n < m:
    for i in range(n,m):
        if i%2 == 1:
            print (i)
            
elif m < n:
    for i in range(m,n):
        if i%2 == 1:
            print (i)
