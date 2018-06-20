m = int(input())
n = int(input())
mult = n
while n%m != 0:
    n-=1
    mult = n
print (mult)
