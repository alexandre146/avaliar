n = int(input())
produto = 1
while 0<=n<=12 and n!=-1:
    
    for i in range(n):
        produto *= i+1
        
    print(produto)
    produto = 1
    n = int(input())