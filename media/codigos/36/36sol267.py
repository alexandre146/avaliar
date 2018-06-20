cont=0
M=int(input())
N=int(input())
maiorMultiplo=N-N%M
if(maiorMultiplo!=0)and(maiorMultiplo<N):
    print(maiorMultiplo)
else:
    print("sem multiplos menores que N")

    
    
