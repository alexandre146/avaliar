

m = int(input())
n = int(input())

for i in range(min(m,n),max(m,n)+1):
    if (i % 2) != 0:
        print (i)
