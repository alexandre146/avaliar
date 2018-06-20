a = int(input())
b = int(input())
c = int(input())
if(a>c or b>c):
    if(a > b):
        tmp = a 
        a = c
        c = tmp
    else:
        tmp = b 
        b = c
        c = tmp
if (a>b):
	tmp = a
	a = b
	b = tmp
print(a)
print(b)
print(c)