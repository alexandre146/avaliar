idade = int(input())

if(idade < 16):
    print("nao eleitor")
elif(idade >=18 and idade <=65):
    print("eleitor obrigatorio")
else:
    (16 <= idade >= 18 or idade > 65)
    print("eleitor facultativo")
