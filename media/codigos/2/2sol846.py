numero1 = 0
numero2 = 0
numero3 = 0

primeiro = 0
segundo = 0
terceiro = 0

print ("digite um numero")
numero1 = int(input())

print ("digite outro numero")
numero2 = int(input())

print ("digite outro numero")
numero3 = int(input())

if numero2 < numero1 > numero3:
  terceiro = numero1
if numero2 == numero1 > numero3:
   terceiro = numero1
if numero2 == numero1 == numero3:
   terceiro = numero1
if numero2 < numero1 == numero3:
   terceiro = numero1
   
if numero2 > numero1 > numero3:
  segundo = numero1
if numero2 < numero1 < numero3:
   segundo = numero1
if numero2 == numero1 < numero3:
   segundo = numero1
if numero2 > numero1 == numero3:
   segundo = numero1

if numero2 > numero1 < numero3:
   primeiro = numero1


if numero1 < numero2 > numero3:
  terceiro = numero2

   
if numero1 == numero2 > numero3:
   segundo = numero2
if numero1 > numero2 == numero3:
   segundo = numero2

if numero1 > numero2 < numero3:
   primeiro = numero2


if numero1 < numero3 > numero2:
   terceiro = numero3

if numero1 < numero3 < numero2:
   segundo = numero3
if numero1 > numero3 > numero2:
   segundo = numero3

if numero1 > numero3 < numero2:
   primeiro = numero3
if numero1 == numero3 == numero2:
   primeiro = numero3
if numero1 == numero3 < numero2:
   primeiro = numero3
if numero1 > numero3 == numero2:
   primeiro = numero3

        

          

print ("\n\n")
print (primeiro)
print (segundo)
print (terceiro)


            
