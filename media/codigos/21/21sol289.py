n = int (input())
m = int (input())
n,m = m,n
while n>m:
    m+=1
    if m % 2 != 0:
        print (m)
