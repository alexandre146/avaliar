a = int (input())
b = 1
cont = 0
while ( b <= a):
     if ( a % b == 0):
          print (b)
          c = b % 3
          if ( c == 0):
               cont = cont + 1
               b = b + 1
          elif (c != 0):
               b = b + 1
     else:
          b = b + 1
if (cont == 0 ):
     print ("O numero nao possui divisores multiplos de 3")
else:
     print (cont)
