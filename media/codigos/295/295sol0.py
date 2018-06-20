import math
x=input()
y=x.split(' ')
x1,y1=int(y[0]),int(y[1])

a=input()
b=a.split(' ')
x2,y2=int(b[0]),int(b[1])

dist= math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))

print('%.4f' %dist)
