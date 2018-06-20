r = 0;
i = 1;
n = int(input())

while(i<= n):
    if(n % i == 0): 
        if(i % 3 == 0): 
            r = r + 1
    i = i + 1
            
if(r == 0):
    print("O numero nao possui divisores multiplos de 3!")
else: 
    print(r)
    




