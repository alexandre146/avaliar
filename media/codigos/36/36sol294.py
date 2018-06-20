N=int(input())
M=int(input())
total=M//N
multiplo=total*N
if N>M:
    print ("sem multiplos menores que",M)
else:
    print (multiplo)
