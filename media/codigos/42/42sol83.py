idade=int(input(""))
if(idade<16):
    print("Nao eleitor")
elif(idade>=18 or idade<=65):
    print("Eleitor obrigatorio")
else:
    print("Eleitor facultativo")
