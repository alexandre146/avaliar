m = int (input())
n = int (input())
c = 0
for i in range (m + 1, n+ 1, 1):
     a = i % m
     if (a ==0):
          c = i
if (c > 0):
     print (c)
else:
     print ("sem multilpos menores que " + str (n))
     
