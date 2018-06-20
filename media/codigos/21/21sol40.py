n = int(input())
m = int(input())
x = n
div = 0
while x <= m:
    div = x % 2
    if(div != 0):
        print(x)
    x+=1
