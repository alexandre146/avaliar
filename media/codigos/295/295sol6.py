x1,y1 = int(input()),int(input())
x2,y2 = int(input()),int(input())
import math
a = (x2-x1)**2
b = (y2-y1)**2
dxy = math.sqrt(a+b)
print ('%.4f'%dxy)
