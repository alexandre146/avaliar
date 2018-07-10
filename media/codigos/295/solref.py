ponto1 = input().split()
ponto2 = input().split()
distancia = pow((pow(float(ponto2[0])-float(ponto1[0]),2) + pow(float(ponto2[1])-float(ponto1[1]),2)), 1/2)
print ("%.4f" % distancia)
