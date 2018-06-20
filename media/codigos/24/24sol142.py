fatorial = int(input())

while fatorial != -1:
    
    multiplicacao = 1
    contador = 1
    
    while fatorial > contador:
        
        contador+=1
        multiplicacao*=contador
        
    print(multiplicacao)
    fatorial = int(input())
