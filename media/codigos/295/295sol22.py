linha = str(input())
linha2 = str (input())
valores = linha.split(" ")
valores2 = linha2.split(" ")
a = int (valores[0])
b = int (valores[1])
c = int (valores2[0])
d = int (valores2[1])
e = (c - a)
f = (d - b)
g = "%.4f" %(((e **2) + (f**2))**(1/2))
print (g)




