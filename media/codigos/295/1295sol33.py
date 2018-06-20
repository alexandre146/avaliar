n1 = input().split(" ")
n2 = input().split(" ")
x1 = int(n1[0])
y1 = int(n1[1])
x2 = int(n2[0])
y2 = int(n2[1])
distancia = ( (x1-x2)**2 + (y1-y2)**2 ) ** 0.5
print("%.4f" % distancia)


