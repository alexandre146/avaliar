idade=int(input())
if(idade<16):
    print('nao eleitor')
elif(idade==16 or idade==17 or idade>65):
    print('eleitor facultativo')
elif(idade>=18 or idade<=65):
    print('eleitor obrigatorio')
