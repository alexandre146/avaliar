a = input()
b = input()
c = input()

if a <= b and b <= c:
    print(a)
    print(b)
    print(c)
elif a >= b and b >= c:
    print(c)
    print(b)
    print(a)
elif a >= b and b <= c:
    print(b)
    print(a)
    print(c)
elif a <= b and b >= c:
    print(a)
    print(c)
    print(b)
        


