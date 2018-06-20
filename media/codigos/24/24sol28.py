n = int(input())
m = int(input())
o = int(input())
if 0 < n <= 12 :
    i = 1
    fat = 1
    while i <= n :
        fat = fat * i
        i = i + 1
    print(fat)
if 0 < m <= 12 :
    i = 1
    fat = 1
    while i <= m :
        fat = fat * i
        i = i + 1
    print(fat)
if 0 < 0 :
    i = 1
    fat = 1
    while i <= 0 :
        fat = fat * i
        i = i + 1
    print(fat)
if n == 0 :
    fat = 0
    print(fat)    
if m == 0 :
    fat = 0
    print(fat)
