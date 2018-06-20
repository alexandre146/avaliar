maior=0

numN=int(input())
numM=int(input())
for i in range(numN,numM+1):
    if(i%numN==0):
        if(i>maior):
            maior=i
if(maior==0):
    print("sem multiplos menores que", numM)
else:
    print(maior)

        
            
    

   
       
