idade = int(input())

if(idade < 16):
    print("nao eleitor")
if(idade >= 16 and idade <= 18):
    print("eleitor facultativo")
if(idade > 18):
    print("eleitor obrigatorio")
