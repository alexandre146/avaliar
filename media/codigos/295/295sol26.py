from math import sqrt
x,y=input()
x2,y2=input()
a=int(x)
b=int(x2)
c=int(y)
d=int(y2)
resx=(b-a)*(b-a)
resy=(d-c)*(d-c)
res=resx+resy
resposta=sqrt(res)
print("%.4f"%resposta)

