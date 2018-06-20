n= int(input())
m= int(input())
if n % 2 != 0 and m % 2 != 0:
    print (min(n,m))
    print(max(n,m))
elif n % 2 != 0 and m % 2 == 0:
    print(n)
else:
    print(m)