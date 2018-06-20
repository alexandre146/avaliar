i = int(input())

if (i < 16):
    print ("nao eleitor")

elif (i >=16 and i < 18 or i > 65):
    print ("eleitor facultativo")
    
elif (18 <= i or i <= 65):
    print ("eleitor")
