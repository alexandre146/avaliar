n=int(input())
if(n<16):
    print('nao eleitor')
elif(n>=18 and n<=65):
    print('eleitor obrigatório')
elif((16<=n<=18) or (n>65)):
    print('eleitor facultativo')
    
