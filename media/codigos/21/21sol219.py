n = int (input())
m = int (input())
a = n % 2
b = m % 2
if (a==0 and b ==0):
     c = n + 1
     for i in range (c,m,2):
          print (i)
elif(a==0 and b==1):
     d = n + 1
     for j in range (d,m+1,2):
          print (j)
elif (a==1 and b ==1):
     e = n
     for k in range (e,m+1,2):
          print (k)
elif (a==1 and b ==0):
     f = n
     for o in range (f, m,2):
          print (o)
