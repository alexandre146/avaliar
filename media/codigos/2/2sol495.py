a = eval(input())
b = eval(input())
if b < a:
   t = b
   b = a
   a = t
c = eval(input())
if c < b:
   t = c
   c = b
   if t < a:
      b = a
      a = t
   else:
      b = t
print("%d\n%d\n%d" %(a, b, c))
