v = input()
u = input()
import math
a = v.split( )
b = u.split( )
x1 = a[0]
y1 = a[1]
x2 = b[0]
y2 = b[1]
x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)
D = (x2-x1)**2
D1 = (y2-y1)**2
D2 = math.sqrt(float(D) + float(D1))
print ('%.4f'%D2)
