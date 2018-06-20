num1 = int(input())
if(num1>=0)and(num1<=12):
    cont = num1
    num = num1
    n = num-1
    while(num1!=-1):
        cont+=1
        while(cont!=0)and(n!=0):
            fatorial = num * (n)
            num = fatorial
            cont-=1
            n-=1
        print(num)
        num1 = int(input())
        cont = num1
        num = num1
        n = num-1
    


