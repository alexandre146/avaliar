result = 0
numM = int(input())
numN = int(input())
if (numM % 2 == 0) and (numN % 2 == 0):
    result = numN // numM
elif (numM % 2 == 1) and (numN % 2 == 0):
    result = (numN - 1) // numM
elif (numM % 2 == 0) and (numN % 2 == 1):
    result = (numN - 1) // numM
elif (numM % 2 == 1) and (numN % 2 == 1):
    result = numN // numM
if (result * numM <= numN):
    result2 = numM * result
    print (result2)
else:
    print ("sem multiplos menores que N")
    









