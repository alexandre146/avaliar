from math import sqrt 
a = input()
a = a.split()
b = input()
b = b.split()
dt = sqrt(pow(float(b[0])-float(a[0]),2)+pow(float(b[1])-float(a[1]),2))
print ("%.4f"%dt)
