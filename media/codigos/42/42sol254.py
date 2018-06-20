idade=int(input(""))
if(idade<16):
    print("nao eleitor")
else:
    if(idade>=18 and idade<=65):
        print("eleitor obrigatorio")
    else:
        print ("eleitor faculativo")
    
