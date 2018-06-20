


n=input()
m=input()

if n > m:
  for i in range(int(m) , int(n)+1):
     if i%2== 1:
        print (i)
else:
  for ii in range(int(n) , int(m)+1):
     if ii%2== 1:
        print (ii)

