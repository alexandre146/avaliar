a = input()
b = input()
c = input()

if a <= b and b <= c:
    print(a)
    print(b)
    print(c)
    if b <= c and c <= a:
        print(b)
        print(c)
        print(a)
        if c <= a and a <= b:
            print(c)
            print(a)
            print(b)
    
   
        


