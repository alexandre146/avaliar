a = int(input())
if (a < 16):
    print("nao eleitor")
elif (a >= 18 and a <= 65): 
    print("eleitor obrigatorio")
else:
    print("eleitor facultativo")
