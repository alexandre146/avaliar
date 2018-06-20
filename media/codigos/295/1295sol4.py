linha = str(input())
linha2 = str (input())
valores = linha.split(" ")
valores2 = linha2.split(" ")
a = int (valores[0])
b = int (valores[1])
c = int (valores2[0])
d = int (valores2[1])
e = "%.4f" % (a - c)
f = "%.4f" % (b - d)
print (str(e),str(f))




