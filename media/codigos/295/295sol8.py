x1,y1 = input()
x2,y2 = input()
import math
a = (x2-x1)**2
b = (y2-y1)**2
dxy = math.sqrt(a+b)
print ('%.4f'%dxy)
