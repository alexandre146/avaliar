entrada = open('3 Numeros em Ordem Crescente.in', 'r')
a = entrada.readline()
b = entrada.readline()
if b < a:
   d = b
   b = a
   a = d
c = entrada.readline()
if c < a:
   d = c
   c = b
   b = a
   a = d
elif c < b:
   d = c
   c = b
   b = d
entrada.close()
saida = open('3 Numeros em Ordem Crescente.out', 'w')
saida.write(a)
saida.write(b)
saida.write(c)
saida.close()
