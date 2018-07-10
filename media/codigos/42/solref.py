idade = int(input())
if (idade < 16) :
    print ("nao eleitor")
elif ( (18 <= idade) and (idade <= 65) ):
    print ("eleitor obrigatorio")
else:
    print ("eleitor facultativo")
