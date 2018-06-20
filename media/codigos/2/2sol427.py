a = int(input())
b = int(input())
c = int(input())
if a < b and a < c and b < c:
    print(a, b, c)
elif a < c and a < b and c < b:
    print(a, c, b)
elif b < a and b < c and a < c:
    print(b, a, c)
elif b < c and b < a and c < a:
    print(b, c, a)
elif c < a and c < b and a < b:
    print(c, a, b)
else:
    if c < b and c < a and b < a:
        print(c, b, a)
    
