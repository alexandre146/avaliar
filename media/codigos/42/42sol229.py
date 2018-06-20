n=int(input())
if(n>=18 and n<=65):
    print("eleitor obrigatorio")
elif(n<16):
    print("nao eleitor")
elif(n>=16 and n<18 or n >65):
    print("eleitor facultativo")
