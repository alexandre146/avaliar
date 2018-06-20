idade = int(input())
if(idade<16):
    print("nao eleior")
elif(idade>=18 and 65<=idade):
    print("eleitor obrigatorio")
else:
    print("eleitor facultativo")
