from math import sqrt
x,y=str(input()).split()
x2,y2=str(input()).split()
a=int(x)
b=int(y)
c=int(x2)
d=int(y2)
resx=(c-a)*(c-a)
resy=(d-b)*(d-b)
res=resx+resy
resposta=sqrt(res)
print("%.4f" %resposta)

