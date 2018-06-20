idade=int(input(""))
if(idade<16):
    print("nao eleitor")
if(idade>=18 and idade<=65):
    print("eleitor obrigatorio")
if(idade==16 or idade==17 or idade>65):
    print ("eleitor faculativo")
    
