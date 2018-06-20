n = int(input ())
m = int(input())
if n > m:
    aux = n
    n = m
    m = aux
while n<=m:
    if n%2 == 1:
        print (n)
    n = n + 1
    
    
    
    


           
