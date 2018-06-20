n=int(input())
if(n<16):
    print("não eleitor")
elif(n>=18 or n<=65):
    print("eleitor obrigatorio")
else:
    print("eleitor facultativo")
