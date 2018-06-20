a = int (input ())
if (a < 16):
     print ("não eleitor")
elif ( 18<= a <=65):
     print ("eleitor obrigatorio")
elif ( 16 <= a <18 or a > 65):
     print ("eleitor facultativo")
