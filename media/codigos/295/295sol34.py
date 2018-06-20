from math import sqrt
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
dist = sqrt(((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1)))
print("%.4f"%dist)