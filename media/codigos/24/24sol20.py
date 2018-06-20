while True:
    n = input()
    if n == -1:
        break
    for p in range(2,n):
        n*=p
    print (n)
