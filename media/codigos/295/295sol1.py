import math

s=str(input())
s=s.split(" ")

r=str(input())
r=r.split(" ")

a = (int(s[0]) - int(r[0]))**2 + (int(s[1])  - int(r[1]))**2
b = math.sqrt(a)

print("%.4f"%b)
