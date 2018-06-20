x1,y1 = input(),input()
x2,y2 = input(),input()
import math
a = int(x2-x1)**2
b = int(y2-y1)**2
dxy = math.sqrt(a+b)
print ('%.4f'%dxy)
