a = 1
fat = 1
n = int(input())
if(n != -1):
    while(a <= n):
        fat = fat*a
        a = a+1
    print(fat)
    print(a)
