n = int(input())
m = int(input())

if n % 2 != 0:
    print(n)

while n in range(n, m + 1):
    n = n + 1
    if n %2 != 0:
        print(n)
    elif n == m:
        break
    

    
    
    
    
