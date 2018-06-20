n = int(input("Coloque os numeros para serem comparados :"))
m = int(input())

if n < m:
    for i in range(n,m+1):
        if i%2 == 1:
            print (i)
            
elif m < n:
    for i in range(m,n+1):
        if i%2 == 1:
            print (i)
