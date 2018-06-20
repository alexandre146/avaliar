primeiro = int(input())
segundo = int(input())
if segundo % primeiro != 0 and primeiro < segundo:
    reduce = segundo - 1
    while reduce % primeiro != 0 and reduce != 0:
        reduce -= 1
    if reduce % primeiro == 0:
        resultado = reduce
    else:
        resultado = "sem multiplos menores que N"
else:
    resultado = "sem multiplos menores que N"
print (resultado)
