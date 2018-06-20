idade=int(input())
if(idade<16):
    print('não eleitor')
elif(16>=idade<18 or idade>65):
    print('eleitor facultativo')

elif(idade>=18 or idade<=65):
    print('eleitor obrigatorio')
