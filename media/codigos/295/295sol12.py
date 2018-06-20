x1,y1 = input()
x2,y2 = input()
import math
a = int(x2-x1)**2
b = int(y2-y1)**2
dxy = math.sqrt(a+b)
print ('%.2f'%dxy)
