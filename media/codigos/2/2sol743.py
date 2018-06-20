a=int(input())
b=int(input())
c=int(input())
if a<b and a<c:
   print (a)
   if b<c:
      print(b)
      print(c)
   elif b>c:
      print(c)
      print(b)
elif b<a and b<c:
    print (b)
    if a<c:
        print(a)
        print(c)
    elif a<c:
        print(c)
        print(a)
elif c<a and c<b:
    print(c)
    if b<a:
        print(b)
        print(a)
    elif a<b:
        print(a)
        print(b)
