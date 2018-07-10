m = int(input())
n = int(input())
if (m > 0 and n > 0) :
    maior_multiplo = -1
    for i in range(n, m-1, -1):
        if (i % m == 0) :
            if (i > maior_multiplo) :
                maior_multiplo = i

if (maior_multiplo == -1) :
    print("sem multiplos menores que %d" % n)
else :
    print(maior_multiplo)
