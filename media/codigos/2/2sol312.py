a=input ()
b=input ()
c=input ()

if (a < c):
    if (a < b): 
        print (a)
        if (b < c):
            print (b)
            print (c)
        else:
            print (c)
            print (b)
    elif (a < c):
        print (b)
        print (a)
        print (c)
    else:
        print (a)
        print (c)
        print (b)
else:
    if (b < c):
        if (b < a):
            print (b)
            if (a < c):
                print (a)
                print (c)
            else:
                print (c)
                print (a)
    else:
        if (c < b):
            if (c < a):
                print (c)
                if (b < a):
                    print (b)
                    print (a)
                else:
                    print (a)
                    print (b)
            else:
                print (a)
                print (c)
                print (b)
        else:
            print (a)
            print (b)
            print (c)
        
    
        
