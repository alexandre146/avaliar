x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
delta_x = x2-x1
delta_y = y2-y1
distancia = ((delta_x**2)+ (delta_y**2))**(1/2)
print("%.4f" %distancia)
