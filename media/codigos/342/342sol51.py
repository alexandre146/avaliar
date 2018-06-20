r = 0
n = int(input())

for i in range(1,n+1):

    if(n % i == 0):
        if(i % 3 == 0):
            r += 1
        
        
if(r > 0):
    print(r,"\n")
else:
    print("O numero não possui divisores multiplos de 3 \n")
