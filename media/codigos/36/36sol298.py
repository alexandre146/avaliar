M=int(input())
N=int(input())
MM=N-N%M
if(MM!=0)and(MM<=N):
    print(MM)
else:
    print("sem multiplos menores que",N)
