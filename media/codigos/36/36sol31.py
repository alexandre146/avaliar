M=int(input())
N=int(input())
k=1
J=0
if(M==N):
    print(N)
if(M<N):
    while(J<N):
        J=M*k
        k=k+1
    print(J-M)
if(M>N):
    print('sem multiplos menores que ', N)
