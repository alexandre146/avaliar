
idade = int(input())

if idade < 16:
    print("nao eleitor")
    
elif 18 <= idade <= 65:
    print("eleitor obrigatorio")
    
elif 18 >= idade >= 16 or idade>= 65:
    print("eleitor facultativo")
    
    