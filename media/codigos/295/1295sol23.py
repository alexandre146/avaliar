X1,Y1 = map(int,input().split())
X2,Y2 = map(int,input().split())
x = (X2-X1)**2
y = (Y2-Y1)**2
D = (x + y)**1/2
print("%.4f"%D)