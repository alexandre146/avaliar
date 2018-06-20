x1, y1 = map(int,input().split())
x2, y2 = map(int,input().split())
dist = (((x2-x1)**2)+((y2-y1)**2))
import math
total = math.sqrt(dist)
print("%.4f" %total)